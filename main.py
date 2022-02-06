from flask import Flask,render_template,request,redirect
from src.indeed import get_jobs as get_indeed_jobs
from src.so import get_jobs as get_so_jobs

app =Flask("SuperScrapper")

db={}

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def report():
  word = request.args.get("word",str)
  if word:
    word = word.lower()
    existing_jobs = db.get(word)
    if existing_jobs:
      all_jobs = existing_jobs
    else:
      indeed_jobs=get_indeed_jobs(word)
      so_jobs =get_so_jobs(word)
      all_jobs= so_jobs + indeed_jobs
      db[word]=all_jobs
    print(all_jobs)
  else:
    return redirect("/")
  return render_template("search.html",userWord=word,resultsNumber=len(all_jobs),jobs=all_jobs)
app.debug = True
app.run(host="0.0.0.0")