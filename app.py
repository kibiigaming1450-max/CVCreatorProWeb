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


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )