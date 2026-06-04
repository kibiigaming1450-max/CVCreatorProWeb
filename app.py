from flask import Flask, render_template, request, send_file
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

cv_data = {}

@app.route("/")
def accueil():
    return render_template("index.html")

@app.route("/generer", methods=["POST"])
def generer():

    global cv_data

    photo = request.files.get("photo")

    photo_filename = ""

    if photo and photo.filename:

        photo_filename = secure_filename(
            photo.filename
        )

        photo.save(
            os.path.join(
                UPLOAD_FOLDER,
                photo_filename
            )
        )

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
        "interets": request.form.get("interets"),
        "theme": request.form.get("theme"),
        "photo": photo_filename
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

    prenom = cv_data.get("prenom", "")
    nom = cv_data.get("nom", "")
    email = cv_data.get("email", "")
    telephone = cv_data.get("telephone", "")
    adresse = cv_data.get("adresse", "")
    profil = cv_data.get("profil", "")
    competences = cv_data.get("competences", "")
    experience = cv_data.get("experience", "")
    formation = cv_data.get("formation", "")
    langues = cv_data.get("langues", "")
    interets = cv_data.get("interets", "")

    titre = f"{prenom} {nom}"

    elements.append(
        Paragraph(
            titre,
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            f"<b>Email :</b> {email}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Téléphone :</b> {telephone}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"<b>Adresse :</b> {adresse}",
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
            profil,
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
            competences,
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
            experience,
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
            formation,
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
            langues,
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
            interets,
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