from fastapi import FastAPI, UploadFile
from pydantic import BaseModel
from fpdf import FPDF
import pandas as pd
import openai, os
from gtts import gTTS
import tempfile

app = FastAPI(title="JanTax Backend")

openai.api_key = os.getenv("OPENAI_API_KEY")

# ---------- ITR ----------
class ITRRequest(BaseModel):
    income: float
    deductions: float
    regime: str = "old"

@app.post("/itrfiling")
def itr(req: ITRRequest):
    taxable = max(0, req.income - req.deductions)
    tax = 0
    if req.regime == "old":
        if taxable <= 250000: tax = 0
        elif taxable <= 500000: tax = (taxable-250000)*0.05
        elif taxable <= 1000000: tax = 12500+(taxable-500000)*0.2
        else: tax = 112500+(taxable-1000000)*0.3
    else:
        if taxable <= 300000: tax=0
        elif taxable <= 600000: tax=(taxable-300000)*0.05
        elif taxable <= 900000: tax=15000+(taxable-600000)*0.1
        elif taxable <= 1200000: tax=45000+(taxable-900000)*0.15
        elif taxable <= 1500000: tax=90000+(taxable-1200000)*0.2
        else: tax=150000+(taxable-1500000)*0.3
    pdf = FPDF(); pdf.add_page(); pdf.set_font("Arial",size=12)
    pdf.cell(200,10,txt=f"ITR Draft - Income: {req.income}, Deductions: {req.deductions}, Tax: {tax}",ln=1)
    pdf.output("ITR_Draft.pdf")
    return {"Income": req.income,"Deductions": req.deductions,"Taxable": taxable,"Tax": tax}

# ---------- GST ----------
class GSTRequest(BaseModel):
    sales: float
    purchases: float

@app.post("/gstfiling")
def gst(req: GSTRequest):
    gst = (req.sales - req.purchases) * 0.18
    df = pd.DataFrame({"Sales":[req.sales],"Purchases":[req.purchases],"GST":[gst]})
    df.to_csv("GST_Draft.csv",index=False)
    return {"Sales": req.sales,"Purchases": req.purchases,"GST": gst}

# ---------- TDS ----------
class TDSRequest(BaseModel):
    salary: float

@app.post("/tdsfiling")
def tds(req: TDSRequest):
    tds = req.salary * 0.1
    with open("TDS_Draft.txt","w") as f: f.write(f"Salary={req.salary}, TDS={tds}")
    return {"Salary": req.salary,"TDS": tds}

# ---------- PT ----------
class PTRequest(BaseModel):
    employees: int

@app.post("/ptfiling")
def pt(req: PTRequest):
    payable = req.employees * 200
    with open("PT_Draft.pdf","w") as f: f.write(f"Employees={req.employees}, PT={payable}")
    return {"Employees": req.employees,"PT": payable}

# ---------- Voice (Multilingual) ----------
@app.post("/voice")
async def voice(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False,suffix=".wav") as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name
    # Use Whisper for STT
    transcript = openai.Audio.transcribe("whisper-1", open(tmp_path,"rb"))
    text = transcript["text"]
    # Convert AI response to TTS
    tts = gTTS(text=text, lang="hi")
    tts.save("voice_reply.mp3")
    return {"transcript": text, "audio_file": "voice_reply.mp3"}
