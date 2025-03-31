try:
  #Execute requested action
  script_name = "entities_aktualisieren.py"
  action = data.get("action", "")

  if action.lower() == "set_state":
    #Parameter -> action: set_state (string, required)
    #Parameter -> entity_id (string, required)
    #Parameter -> state (string, required)
    
    #Getting entity
    entity_id = data.get("entity_id", "")

    #Getting original state and attributes
    entity = hass.states.get(entity_id)

    attributes = {}
    for attr in entity.attributes:
      attributes[attr] = entity.attributes.get(attr)

    #Getting new state
    new_state = data.get("state", "")

    #Setting new state
    hass.states.set(entity_id, new_state, attributes)

  elif action.lower() == "set_attributes":
    #Parameter -> action: set_attributes (string, required)
    #Parameter -> entity_id (string, required)
    #Parameter -> attributes (list, required)

    #Getting entity
    entity_id = data.get("entity_id", "")

    #Getting original state and attributes
    entity = hass.states.get(entity_id)
    state = entity.state
    attributes = {}
    for attr in entity.attributes:
      attributes[attr] = entity.attributes.get(attr)

    #Getting new attributes
    new_attributes = data.get("attributes", "")

    #Setting new attributes
    for new_attr in new_attributes:
      for k,v in new_attr.items(): #This should iterate just once
        attributes[k] = v
    hass.states.set(entity_id, state, attributes)

  elif action.lower() == "set_state_attributes":
    #Parameter -> action: set_state_attributes (string, required)
    #Parameter -> entity_id (string, required)
    #Parameter -> state (string, required)
    #Parameter -> attributes (list, required)

    #Getting entity
    entity_id = data.get("entity_id", "")

    #Getting original state and attributes
    entity = hass.states.get(entity_id)

    state = entity.state
    attributes = {}
    for attr in entity.attributes:
      attributes[attr] = entity.attributes.get(attr)
      
    #Getting new state
    new_state = data.get("state", "")

    state = new_state
    #Setting new state

    #Getting new attributes
    new_attributes = data.get("attributes", "")

    #Setting new attributes
    for new_attr in new_attributes:
      for k,v in new_attr.items(): #This should iterate just once
        attributes[k] = v
    hass.states.set(entity_id, state, attributes)


except Exception as e:
  logger.error("**An unhandled error has occurred.**\n\n{}".format(e))
