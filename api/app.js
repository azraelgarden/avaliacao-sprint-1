const Database = require('./mongodb/mongo')
const express = require('express')
const cors = require('cors')
const app = express()

app.use(cors())
app.use(express.urlencoded({extended:false}))
app.use(express.json())

app.get('/:login', async(req, res)=> {
    const database = new Database()
    const { login } = req.params
    const result = await database.find(login)
    console.log(result)
    res.send(result)
})

app.listen(3000, ()=> {
    console.log('servidor rodando')
})