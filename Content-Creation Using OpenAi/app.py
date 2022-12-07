from flask import Flask, render_template, request
import config
import aicontent
def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])
app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())



@app.route('/product-description', methods=["GET", "POST"])
def productDescription():

    if request.method == 'POST':
        submission = request.form['productDescription']
        part1 = aicontent.OpenAiQuery(
            'Create an Instagram caption for image: {}. \n'.format(submission))
        part2 = aicontent.OpenAiQuery(
            'generate Instagram hashtags for: {}'.format(submission))
        openAIAnswer = """
        {}
        
        {}
        """.format(part1,part2)
        prompt = 'AI Suggested caption for {} are:'.format(submission)

    return render_template('product-description.html', **locals())



@app.route('/funny-pickupline', methods=["GET", "POST"])
def funnyPickupline():

    if request.method == 'POST':
        submission = request.form['funnyPickupline']
        query = "Write a funny pickup line for : {}".format(submission)
        openAIAnswer = aicontent.OpenAiQuery(query)
        prompt = 'AI Suggested PickUp Line for {} are:'.format(submission)
    return render_template('funny-pickupline.html', **locals())


@app.route('/cold-emails', methods=["GET", "POST"])
def coldEmails():

    if request.method == 'POST':
       submission = request.form['coldEmails']
       query = "Write a cold email for: {}".format(submission)
       openAIAnswerUnformatted = aicontent.OpenAiQuery(query)
       openAIAnswer = openAIAnswerUnformatted.replace("\n",'<br>')
       prompt = 'AI Suggested Email Template for {} are:'.format(submission)
    return render_template('cold-emails.html', **locals())


@app.route('/pcode', methods=["GET", "POST"])
def code():

    if request.method == 'POST':
       submission = request.form['code']
       query = "{}".format(submission)
       openAIAnswerUnformatted = aicontent.OpenAiQuery(query)
       openAIAnswer = openAIAnswerUnformatted.replace("\n", '<br>')
       prompt = 'AI Suggested Code for {} are:'.format(submission)
    return render_template('pcode.html', **locals())


@app.route('/video-ideas', methods=["GET", "POST"])
def videoIdeas():

    if request.method == 'POST':
        submission = request.form['videoIdeas']
        query = "Generate some video ideas for : {}".format(submission)
        openAIAnswer = aicontent.OpenAiQuery(query)
        prompt = 'AI Generated Ideas for {} are:'.format(submission)
    return render_template('video-ideas.html', **locals())


@app.route('/video-description', methods=["GET", "POST"])
def videoDescription():

    if request.method == 'POST':
        submission = request.form['videoDescription']
        query = "Generate a video description for : {}".format(submission)
        openAIAnswer = aicontent.OpenAiQuery(query)
        prompt = 'AI Suggested Description for {} are:'.format(submission)
    return render_template('video-description.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
