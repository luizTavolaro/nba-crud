# POST
curl -X POST http://ec2-18-205-194-110.compute-1.amazonaws.com:30000/times \
  -H "Content-Type: application/json" \
  -d '{
    "id": 6,
    "nome": "Chicago Bulls",
    "cidade": "Chicago",
    "dataFundacao": "1966-01-16",
    "tecnico": "Billy Donovan"
}';

# GET
curl http://ec2-18-205-194-110.compute-1.amazonaws.com:30000/times;

#PUT 
curl -X PUT http://ec2-18-205-194-110.compute-1.amazonaws.com:30000/times/6 \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "Chicago Bulls Atualizado",
    "cidade": "Chicago",
    "dataFundacao": "1966-01-16",
    "tecnico": "Novo Técnico"
}';

#DELETE 
curl -X DELETE http://ec2-18-205-194-110.compute-1.amazonaws.com:30000/times/6;
