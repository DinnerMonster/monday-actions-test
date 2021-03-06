# All data is type string.
def monday_board_get(id):
    boards = ("""
    {
        boards (ids:%s){
            name
        }
    }
    """) % (id)
    
    return boards
#Posts cannot contain spaces in the name.
def monday_board_post(name, kind): #kind = public or private
    post = ("""
    mutation {
    create_board (board_name: %s, board_kind: %s) {
    id
    }
    }""") % (name,kind)
    return post
def monday_board_groups(id):
    groups = """mutation {
    boards (ids: %s) {
    groups {
    id
    title
    color
    position
    }
    }
    }""" % (id)
    return groups

def monday_board_item_get(id):
    item = ("""{
        boards (ids:%s){
             items{
                name
                }
            }
        }
    """) % (id)   
    return item
def monday_item_get(limit): #gets all items in account.
    items = ("""
        query {
            items (limit: %s) {
            id
            name
            board {
            id
            }
            creator {
            id
                    }
                }
            }
            """) % (limit)
    return items
def monday_item_post(id,group_id,item_name):
    post =  (""" mutation {
    create_item (board_id:%s, group_id: %s, item_name: %s) {
    id
    }
    }""") % (id,group_id,item_name)
    return post

def monday_board_update_get(id,limit):
    update = ("""
    query {
        boards(ids:%s) {
        updates (limit: %s) {
        id
        body
            }
        }
        """) % (id,limit)
    return update
def monday_board_update_group_get(id,group_id,limit):
    update = ("""
    query {
        boards(ids: %s) {
            groups (ids: %s)
        updates (limit: %s) {
        id
        body
                }
            }
        }
        """) % (id, group_id, limit)
    print('Returned ' + limit + ' updates.')
    return update
def monday_board_group_get(id):
    group = ("""
    {
        boards (ids:%s){
            groups {
                title
                id
            }
        }
    }
    """) % (id)
    
    return group