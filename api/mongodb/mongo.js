const { MongoClient } = require("mongodb");

const uri ='mongodb://leonardo:saturno@127.0.0.1:27017?writeConcern=majority&poolSize=20';

class Database {
   
    createConnection() {
        const client = new MongoClient(uri, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
        });
        return client
    }

    async find(login) {
        const client = this.createConnection()
        try {
            await client.connect()
            
            //db
            const database = client.db("githubUsers");
            //collection
            const users = database.collection("users");

            const query = {login};
            const options = {}

            const user = await users.findOne(query, options)
            return user
        }catch(e) {
            console.error(e)
            return {}
        }finally {
            await client.close();
        }
    }
}

module.exports = Database