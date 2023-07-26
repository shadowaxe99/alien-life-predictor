```python
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class LicensingData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dataset_name = db.Column(db.String(120), unique=True, nullable=False)
    licensee = db.Column(db.String(120), nullable=False)
    license_start_date = db.Column(db.DateTime, nullable=False)
    license_end_date = db.Column(db.DateTime, nullable=False)

db.create_all()

class LicensingSchema(Schema):
    id = fields.Int()
    dataset_name = fields.Str()
    licensee = fields.Str()
    license_start_date = fields.DateTime()
    license_end_date = fields.DateTime()

licensing_schema = LicensingSchema()

@app.route('/license', methods=['POST'])
def create_license():
    data = request.get_json()
    new_license = LicensingData(
        dataset_name=data['dataset_name'],
        licensee=data['licensee'],
        license_start_date=data['license_start_date'],
        license_end_date=data['license_end_date']
    )
    db.session.add(new_license)
    db.session.commit()
    licensing_data = licensing_schema.dump(new_license)
    return {'message': 'LicenseCreated', 'data': licensing_data}, 201

if __name__ == '__main__':
    app.run(debug=True)
```