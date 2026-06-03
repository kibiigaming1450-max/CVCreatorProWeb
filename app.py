from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

app = Flask(__name__) 

cv_data = {}

@app.route("/")
def accueil():
       return 
render_template("index.html")

@app.route("/generer", methods=["POST"])
def generer():

       global cv_data

cv_data = {
    "nom": request.form.get("nom"),
    "prenom": request.form.get("prenom"),
    "email": request.form.get("email"),
    "telephone": request.form.get("telephone"),
    "adresse": request.form.get("adresse"),
    "profil": request.form.get("profil"),
    "competences": request.form.get("competences"),
    "experience": request.form.get("experience"),
    "formation": request.form.get("formation"),
    "langues": request.form.get("langues"),
    "interets": request.form.get("interets")
}

return render_template(
    "resultat.html",
    **cv_data
)

@app.route("/pdf")
def pdf():

       pdf_path = "cv.pdf"

doc = SimpleDocTemplate(pdf_path)

styles = getSampleStyleSheet()

elements = []

elements.append(
    Paragraph(
        f"{cv_data.get('prenom','')} {cv_data.get('nom','')}",
        styles["Title"]
    )
)

elements.append(
    Spacer(1, 15)
)

elements.append(
    Paragraph(
        f"<b>Email :</b> {cv_data.get('email','')}",
        styles["BodyText"]
    )
)

elements.append(
    Paragraph(
        f"<b>Téléphone :</b> {cv_data.get('telephone','')}",
        styles["BodyText"]
    )
)

elements.append(
    Paragraph(
        f"<b>Adresse :</b> {cv_data.get('adresse','')}",
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 15)
)

elements.append(
    Paragraph(
        "PROFIL",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("profil",""),
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 10)
)

elements.append(
    Paragraph(
        "COMPÉTENCES",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("competences",""),
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 10)
)

elements.append(
    Paragraph(
        "EXPÉRIENCE",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("experience",""),
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 10)
)

elements.append(
    Paragraph(
        "FORMATION",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("formation",""),
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 10)
)

elements.append(
    Paragraph(
        "LANGUES",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("langues",""),
        styles["BodyText"]
    )
)

elements.append(
    Spacer(1, 10)
)

elements.append(
    Paragraph(
        "CENTRES D'INTÉRÊT",
        styles["Heading2"]
    )
)

elements.append(
    Paragraph(
        cv_data.get("interets",""),
        styles["BodyText"]
    )
)

doc.build(elements)

return send_file(
    pdf_path,
    as_attachment=True,
    download_name="MonCV.pdf"
)

if __name__ == "__main__":
app.run(
host="0.0.0.0",
port=5000,
debug=True
)