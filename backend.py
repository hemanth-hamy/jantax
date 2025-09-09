from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
import pandas as pd
import whisper
from fpdf import FPDF

app = FastAPI(title="JanTax Drafting Engine")

class TaxInput(BaseModel):
    income: float = 0
    deductions: float = 0

def export_files(data: dict, name: str):
    # CSV
    pd.DataFrame([data]).to_csv(f"{name}.csv", index=False)
    # TXT
    with open(f"{name}.txt", "w") as f:
        for k, v in data.items():
            f.write(f"{k}: {v}\n")
    # PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for k, v in data.items():
        pdf.cell(200, 10, txt=f"{k}: {v}", ln=True)
    pdf.output(f"{name}.pdf")

@app.post("/draft/itr")
def draft_itr(data: TaxInput):
    taxable = max(data.income - data.deductions, 0)
    draft = {
        "type": "ITR",
        "income": data.income,
        "deductions": data.deductions,
        "taxable": taxable
    }
    export_files(draft, "ITR_DRAFT")
    return draft

@app.post("/draft/gst")
def draft_gst():
    draft = {"type": "GST", "status": "Prepared"}
    export_files(draft, "GST_DRAFT")
    return draft

@app.post("/draft/tds")
def draft_tds():
    draft = {"type": "TDS", "status": "Prepared"}
    export_files(draft, "TDS_DRAFT")
    return draft

@app.post("/draft/pt")
def draft_pt():
    draft = {"type": "PT", "status": "Prepared"}
    export_files(draft, "PT_DRAFT")
    return draft

@app.post("/voice")
async def voice_assistant(file: UploadFile):
    model = whisper.load_model("tiny")
    audio = await file.read()
    with open("temp.wav", "wb") as f:
        f.write(audio)
    result = model.transcribe("temp.wav")
    return {"transcript": result["text"]}
