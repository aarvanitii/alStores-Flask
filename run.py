from flask import Flask, url_for, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    info = [
        {
            'label': 'Contact',
            'data_1': 'Telephone',
            'description_1': '8:30 - 20:30',
            'data_2': 'e-Mail',
            'description_2': 'Anytime',
            'data_3': '',
            'description_3': ''
        },
        {
            'label': 'Services',
            'data_1': 'Commande',
            'description_1': '',
            'data_2': 'Conseil',
            'description_2': '',
            'data_3': 'Monter',
            'description_3': ''
        },
        {
            'label': 'Plan Tarifaire',
            'data_1': 'Standard',
            'description_1': '100$',
            'data_2': 'Premium',
            'description_2': '360$',
            'data_3': 'Coutume',
            'description_3': 'Negociable'
        }

    ]

    services = [
        {
            'label': 'Commande',
            'description': 'lorem ipsum monum.',
            'imgUrl': 'static/img/icons/order.png'
        },
        {
            'label': 'Conseil',
            'description': 'lorem ipsum monum.',
            'imgUrl': 'static/img/icons/idea.png'
        },
        {
            'label': 'Monter',
            'description': 'lorem ipsum monum.',
            'imgUrl': 'static/img/icons/installi.png'
        }
    ]

    contacts = [
        {
            'label': 'e-Mail',
            'description': 'Arvanitgrainca.ag@gmail.com.',
            'imgUrl': 'static/img/icons/mail.png',
            'buttonAllow': True
        },
        {
            'label': 'Telephone',
            'description': '+37745609494',
            'imgUrl': 'static/img/icons/phone.png'
        }
    ]    
    return render_template('index.html', info=info, services=services, contacts=contacts)