def options_lister(labels, values):
    options = []
    for i in range(len(labels)):
            option = {
                "text": {
                    "type" : "plain_text",
                    "text": labels[i]
                },
                "value": values[i]
            }
            options.append(option)
    return options

def dropdown_input_creator(id, text, option_labels, option_values):
    options = options_lister(option_labels, option_values)
    block = {
            "type": "input",
            "block_id": id,
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": text,
				},
            "options": options,
            "action_id": id,
			},
			"label": {
				"type": "plain_text",
				"text": text
		    }
        }
    return block

def mrkdwn_block_creator(text): #TODO: use this somewhere. add some more sparkle to the questions perhaps..?
     block = {
          "type": "section",
          "text" : {
               "type" : "mrkdwn",
               "text" : text,
          }
     }
     return block

def get_carb(body):
     carb = body["view"]["state"]["values"]["get_carb"]["get_carb"]["selected_option"]["value"]
     return carb

def get_protein(body):
     protein = body["view"]["state"]["values"]["get_meat"]["get_meat"]["selected_option"]["value"]
     return protein

def meat_getter(ack, labels: list, values: list):
    ack(response_action="push", view={
                "type": "modal",
                "callback_id": "get_meat",
                "title": {"type": "plain_text", "text": "Task"},
                "submit": {"type": "plain_text", "text": "Submit!"},
                "close" : {"type": "plain_text", "text": "Back"},
                "blocks": [
                    dropdown_input_creator("get_meat", "Choose a protein.", labels, values)
                ]
            })
def return_food(carb, protein):
    match carb:
        case "flatbread":
            if protein == "lamb" or protein == "chicken":
                 meal = "greek food or indian food?"
            if protein == "pork":
                 meal = "mexican food?"
        case "pasta":
            if protein == "lamb":
                  meal = "chinese noodles or mediterranean food?"
            if protein == "pork":
                  meal = "i don't know why i made this an option. nobody eats this."
            if protein == "chicken":
                  meal = "italian food or thai food or perhaps chinese food?"
        case "rice":
            if protein == "fish":
                  meal = "japanese food?"
            if protein == "beef":
                  meal = "korean food?"
            if protein == "chicken":
                meal = "mexican food?"
        case "potatoes":
            if protein == "fish":
                 meal = "british food :face_vomiting:"
            if protein == "beef":
               meal = "a burger? or a steak for lunch? how indulgent of you, fat cat."   
            if protein == "chicken":
                meal = "a fast food chicken sandwich?"
    return meal
    
