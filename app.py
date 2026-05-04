from flask import Flask, render_template, request
from services.content_based_filtering import content_based_filtering
from data.data_preprocessing import clean_data, get_top_cpus
from services.topsis import topsis_method

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = clean_data()
    #default table with CPU by performance order
    top_cpus = get_top_cpus().to_dict(orient='records')

    result = None
    user_features = None
    searched = False
    if request.method == "POST":
        user_features = {
            "brand": request.form.get("brand") or None,
            "model": request.form.get("cpuName") or None,
            "category": request.form.get("category") or None,
            "budget": int(request.form.get("budget")),
            "performance": int(request.form.get("cpuMark")),
            "cores": int(request.form.get("cores"))
        }

        result = content_based_filtering(user_features)
        if result is not None and not result.empty:
            result = topsis_method(result)
        else:
            result = []
        searched = True

    return render_template("index.html",
            searched=searched,
            result=result,
            data=data.to_dict(orient='records'),
            top_cpus=top_cpus,
            user=user_features
    )

if __name__ == "__main__":
    app.run(debug=True)





