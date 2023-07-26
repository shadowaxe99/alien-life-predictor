```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), unique=True, nullable=False)
    plan = db.Column(db.String(50), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)

class SubscriptionSchema(Schema):
    id = fields.Int()
    user_id = fields.Str()
    plan = fields.Str()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

subscription_schema = SubscriptionSchema()
subscriptions_schema = SubscriptionSchema(many=True)

@app.route('/subscription', methods=['POST'])
def create_subscription():
    user_id = request.json['user_id']
    plan = request.json['plan']
    start_date = request.json['start_date']
    end_date = request.json['end_date']
    
    new_subscription = Subscription(user_id, plan, start_date, end_date)
    
    db.session.add(new_subscription)
    db.session.commit()

    return subscription_schema.jsonify(new_subscription)

@app.route('/subscription/<id>', methods=['GET'])
def get_subscription(id):
    subscription = Subscription.query.get(id)
    return subscription_schema.jsonify(subscription)

@app.route('/subscription/<id>', methods=['PUT'])
def update_subscription(id):
    subscription = Subscription.query.get(id)

    user_id = request.json['user_id']
    plan = request.json['plan']
    start_date = request.json['start_date']
    end_date = request.json['end_date']

    subscription.user_id = user_id
    subscription.plan = plan
    subscription.start_date = start_date
    subscription.end_date = end_date

    db.session.commit()

    return subscription_schema.jsonify(subscription)

@app.route('/subscription/<id>', methods=['DELETE'])
def delete_subscription(id):
    subscription = Subscription.query.get(id)
    db.session.delete(subscription)
    db.session.commit()

    return subscription_schema.jsonify(subscription)

if __name__ == '__main__':
    app.run(debug=True)
```