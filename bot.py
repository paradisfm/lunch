from config import *
from helpers import *

@bolt_app.command("/lunch")
def question_one(ack, body):
    ack()
    slack_client.views_open(
        trigger_id=body["trigger_id"],
        view = {
            "type": "modal",
            "callback_id": "carb",
            "title": {"type": "plain_text", "text": "What's for lunch?"},
            "submit": {"type": "plain_text", "text": "Next"},
            "close" : {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                dropdown_input_creator("get_carb", "Choose a carb.", ["Flatbread", "Rice", "Pasta", "Potatoes"], ["flatbread", "rice", "pasta", "potatoes"])
            ]
        }
    )

@bolt_app.view("carb")
def question_two(ack, body):
    ack()
    global carb #note: don't do this in production
    carb = get_carb(body)
    if carb in ["rice", "potatoes"]:
            meat_getter(ack, labels=["Fish", "Beef", "Chicken"], values=["fish", "beef", "chicken"])
    if carb in ["pasta", "flatbread"]:
            meat_getter(ack, labels=["Lamb", "Pork", "Chicken"], values=["lamb", "pork", "chicken"])

@bolt_app.view("get_meat")
def submit(ack, body):
    try:
        ack(response_action="clear")
        user = body["user"]["id"]
        protein = get_protein(body)
        meal = return_food(carb, protein)
        slack_client.chat_postMessage(token=config["slack_bot_token"], 
                                       channel=f"@{user}",
                                       text=f"would you go for {meal}",
                                       user=user)
        #TODO: add a yes/no button and come up with option 2 after asking to choose from a variety of other foods like eggs, vegetables, deli meat, beans, etc. 
    except Exception as e:
        slack_client.chat_postMessage(token=config["slack_bot_token"], 
                                      channel=f"@{user}",
                                      text=f"error: {e}",
                                      user=user)

#TODO: app home opened
if __name__ == "__main__":
    socket_mode_handler.connect()
    flask_app.run(host="0.0.0.0", port=8080)