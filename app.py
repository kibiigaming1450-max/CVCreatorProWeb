from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from flask import send_file 
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/generer", methods=["POST"])
def generer():

    nom = request.form.get("nom")
    prenom = request.form.get("prenom")
    email = request.form.get("email")
    telephone = request.form.get("telephone")
    adresse = request.form.get("adresse")

    profil = request.form.get("profil")
    competences = request.form.get("competences")
    experience = request.form.get("experience")
    formation = request.form.get("formation")
    langues = request.form.get("langues")
    interets = request.form.get("interets")

    return render_template(
        "resultat.html",
        nom=nom,
        prenom=prenom,
        email=email,
        telephone=telephone,
        adresse=adresse,
        profil=profil,
        competences=competences,
        experience=experience,
        formation=formation,
        langues=langues,
        interets=interets
    )
@app.route("/pdf")
def pdf():

    pdf_path = "cv.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "CV Creator Pro",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 20)
    )

    elements.append(
        Paragraph(
            "Votre CV généré depuis le site.",
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return send_file(
        pdf_path,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )