import openai
import os
import docx
import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Frame, PageTemplate, Image
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

# Set up your Azure OpenAI Service credentials
openai.api_type = "azure"
openai.api_base = "<API_BASE>"
openai.api_version = "<API_VERSION>"
openai.api_key = "<API_KEY>"

def analyze_risk(risk_description, user_decision):
    prompt = (
        f"Analyze the following risk ({risk_description}) and provide a detailed explanation on whether it should be accepted or rejected "
        f"based on the user's decision ({user_decision}). Include as much detail as possible about the analysis process "
        f"and the conclusions. Also, provide a summary of the factors involved in the risk, including their importance in the format 'Factor: Importance'."
    )
    
    try:
        response = openai.Completion.create(
            engine="threat_model",  # Ensure this is the correct deployment name
            prompt=prompt,
            max_tokens=1000  # Increase the max tokens to allow for a more detailed response
        )
        return response.choices[0].text.strip()
    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"

def analyze_risk_from_docx(file_path, user_decision):
    doc = docx.Document(file_path)
    risk_description = "\n".join([para.text for para in doc.paragraphs])
    
    result = analyze_risk(risk_description, user_decision)
    return risk_description, result

def extract_factors(result):
    # Print the result for debugging purposes
    print("Analysis Result:\n", result)
    
    # Extract factors and their importance from the result using regex
    factors = {}
    factor_pattern = re.compile(r"(\w+):\s*(\d+)")
    matches = factor_pattern.findall(result)
    for match in matches:
        factor, importance = match
        factors[factor] = int(importance)
    
    # If no factors were found, try a different pattern
    if not factors:
        factor_pattern = re.compile(r"(\w+)\s*-\s*Importance:\s*(\d+)")
        matches = factor_pattern.findall(result)
        for match in matches:
            factor, importance = match
            factors[factor] = int(importance)
    
    # If still no factors, try another pattern
    if not factors:
        lines = result.split('\n')
        for line in lines:
            parts = line.split(':')
            if len(parts) == 2:
                factor = parts[0].strip()
                try:
                    importance = int(parts[1].strip())
                    factors[factor] = importance
                except ValueError:
                    continue
    
    # Filter out any lines that contain code or irrelevant content
    filtered_factors = {k: v for k, v in factors.items() if not re.search(r'[^\w\s]', k)}
    
    print("Extracted Factors:\n", filtered_factors)  # Debugging print statement
    return filtered_factors

def generate_heatmap(factors, output_path):
    # Convert factors to a DataFrame
    df = pd.DataFrame(list(factors.items()), columns=['Factor', 'Importance'])
    
    if df.empty:
        raise ValueError("No factors found to plot in the heatmap.")
    
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.set_index('Factor').T, annot=True, cmap="YlGnBu", cbar=True)
    plt.title('Risk Factors Heatmap')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def save_result_to_pdf(risk_description, user_decision, result, factors, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Risk Analysis Report", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Risk Description:", styles['Heading2']))
    story.append(Paragraph(risk_description, styles['BodyText']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("User Decision:", styles['Heading2']))
    story.append(Paragraph(user_decision, styles['BodyText']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Analysis Process and Conclusions:", styles['Heading2']))
    story.append(Paragraph(result, styles['BodyText']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Risk Factors Summary:", styles['Heading2']))

    # Generate and add the heatmap
    heatmap_path = "risk_factors_heatmap.png"
    generate_heatmap(factors, heatmap_path)
    story.append(Image(heatmap_path, width=500, height=300))

    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id='normal')
    template = PageTemplate(id='test', frames=frame)
    doc.addPageTemplates([template])
    
    doc.build(story)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
    if file_path:
        user_decision = decision_var.get()
        risk_description, result = analyze_risk_from_docx(file_path, user_decision)
        
        # Extract factors from the result
        factors = extract_factors(result)
        
        if not factors:
            messagebox.showwarning("No factors found", "No factors were found in the analysis result.")
            return
        
        output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if output_path:
            save_result_to_pdf(risk_description, user_decision, result, factors, output_path)
            messagebox.showinfo("Success", f"Result saved to {output_path}")
        else:
            messagebox.showwarning("No file selected", "Please select a location to save the PDF.")
    else:
        messagebox.showwarning("No file selected", "Please select a Word document.")

# Create the GUI
root = tk.Tk()
root.title("Risk Acceptance Analyzer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

decision_var = tk.StringVar(value="Accept")

accept_radio = tk.Radiobutton(frame, text="Accept", variable=decision_var, value="Accept")
accept_radio.pack(anchor=tk.W)

reject_radio = tk.Radiobutton(frame, text="Reject", variable=decision_var, value="Reject")
reject_radio.pack(anchor=tk.W)

open_button = tk.Button(frame, text="Open File", command=open_file)
open_button.pack(pady=5)

result_label = tk.Label(frame, text="Risk Analysis Result: ")
result_label.pack(pady=5)

root.mainloop()