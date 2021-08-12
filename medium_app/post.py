import frappe
from medium import Client
# for referance 
# https://github.com/Porter97/Python-Medium


def mediumpost(doc,method):
    medium_credential=frappe.get_single('Medium Credential')
   
    token = medium_credential.get_password('token')
    passw = medium_credential.get_password('user_password')
    name = medium_credential.user_id
    # print(token,passw,name)
    
    print(doc.name,doc.content)
    try:
        
        client = Client(application_id=name, application_secret=passw,access_token=token)

        user = client.get_current_user()
        print(user)

        post = client.create_post(user_id=user["id"], title=doc.name, content=doc.content,
                                content_format="html", publish_status=doc.public_status, publication_id=None,
                                notify_followers=True)
        

        frappe.msgprint(msg = 'Post has been created',
                                title = 'Message',
                                indicator = 'green')

        return
    except:
        frappe.msgprint(msg = 'Something Went Wrong',
                                    title = 'Message',
                                    indicator = 'red')




# for further use
# feed = client.list_articles(user['username'])

# print(feed[1])

	

