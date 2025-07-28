# Adobe Hackathon Round 1B - Persona-Driven Intelligence

## 🔍 Task

Extract and rank sections from 3–10 PDFs based on a given persona and job-to-be-done.

## 📁 Input

- input/persona.txt → Line 1 = Persona, Line 2 = Job
- input/docs/ → Place 3–10 PDF documents here

## 📤 Output

- output/round1b_output.json → Top ranked sections

## 🐳 Docker Commands

Build:
```bash
docker build --platform linux/amd64 -t adobehack:round1b .
