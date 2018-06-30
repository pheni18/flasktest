from flask import Flask, render_template, request, redirect, url_for
# Jsonを扱うライブラリ
import json

app = Flask(__name__)

def get_profile():
    # JSONファイルの読み込み
    file_json = 'data/profile.json'
    prof = open(file_json,encoding='utf-8')
    json_str = prof.read()
    prof.close()

    # JSONから辞書型に変換
    prof_dict = json.loads(json_str)
    return prof_dict

def update_profile(prof):
    f = open('data/profile.json', 'w')
    json.dump(prof, f)
    f.close()

@app.route('/get')
def get():
    # GETリクエストを格納
    name = request.args.get('name')
    return render_template('get.html', title='Flask GET request', name=name)

@app.route('/profile')
def profile():
    prof_dict = get_profile()
    print(prof_dict)
    return render_template('profile.html', title='json', user=prof_dict)

@app.route('/edit')
def edit():
    prof_dict = get_profile()
    return render_template('edit.html', title='json', user=prof_dict)

@app.route('/update', methods=['POST'])
def update():
    prof_dict = get_profile()
    # prof_dictの値を変更
    prof_dict['name'] = request.form['name']
    prof_dict['age'] = request.form['age']
    prof_dict['sex'] = request.form['sex']

    update_profile(prof_dict)

    return redirect(url_for("profile"))


if __name__ == '__main__':
    app.run(debug=True)
