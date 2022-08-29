from flask import Flask

from prisma import Prisma, register
from prisma.models import User

app = Flask(__name__)

db = Prisma()
db.connect()
register(db)

@app.route('/', methods = ['GET'])
def getAllUser():
    users = db.user.find_many()
    print(users)
    return 'All user'

@app.route('/', methods = ['POST'])
def createUser():
    create = db.user.create(
        {
            'name': 'imran',
            'email': 'imran@cdda.io'
        }
    )
    return 'Create user'



if __name__ == '__main__':
    app.run(debug=True)
