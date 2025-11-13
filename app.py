from flask import Flask, render_template, request, redirect, url_for
import requests
import os

app = Flask(__name__)

JAVA_CRED_URL = os.getenv("JAVA_CRED_URL", "http://localhost:8081/generate")

@app.route("/", methods=["GET"])
def index():
    return redirect(url_for("issue_credential"))

@app.route("/issue", methods=["GET", "POST"])
def issue_credential():
    if request.method == "POST":
        name = request.form.get("name")
        org = request.form.get("organization")
        ID = request.form.get("ID")

        payload = {"name": name, "organization": org, "ID": ID}

        try:
            res = requests.post(JAVA_CRED_URL, json=payload)
            res.raise_for_status()
            credential_blob = res.text
        except Exception as e:
            return f"Error contacting credential service: {e}", 500

        return render_template("issued_credential.html",
                               name=name,
                               org=org,
                               ID=ID,
                               credential_blob=credential_blob)
    return render_template("issue_form.html")

    from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

JAVA_AUTH_URL = "https://your-auth-server/login"  # Replace with actual URL



if __name__ == "__main__":
    app.run(debug=True)
