Database System

This is a "blank slate" version of a client database system I was contracted to build for a Ltd damp proofing company,
with all company specific information removed and replaced with generic images, info etc.
They had a very specific vision of the layout and flow of the application which I was able to realise when engineering
this system. The system contains all the features that the client requested, including a search function, ability to add
notes and nicknames to each unique customer account, tracking each customers unique progress during the job process,
the ability to change client details after they've been added, a unique reference number added to each client, ability 
to back up the databases and recover in the event they're corrupted, a favourites list where they can store clients to 
re use on adding a new job to the system, a unique, modifiable database of materials and labour, including costs for 
each client and the ability to work out total costs, amount owing, amount paid etc.

Flow of the System

Each client added to the database has a simple flow following the clients vision. The customer details are added to the database, 
where the client can make a choice on whether they want to add to the favourite list. Once the client has been added the
details can be accessed by selecting them from a list of all customers. The client then adds material and labour costs,
adds customer nickname(optional) and notes(optional) then marks customer as quote sent. The total, amount outstanding
and date sent will be added to client information.
At this point the customer will show up in both the "all clients" list and the "quotes pending" list. All data saved
for this customer is modifiable by selecting the change client info option from the options menu. The customer can then
be marked as either "quote accepted" or "quote declined", adding this customer to the quotes accepted list if quotes
accepted was selected. Client can then mark customer as "invoice sent", at which point they will move to the awaiting 
payment list and customer info will show the date invoice was sent. Once customer has paid in full the client will "mark as paid",
where the customer will move to the completed jobs list and customer info will show the date that payment was received
in full. At any point the customers notes and materials and labour can be viewed in full. 

Functions Bound To Keyboard

Pressing ENTER on the add new clients screen will open up the favourites list. Here the client can select a favourite
customer from the list and use their contact info for a new entry.

Holding SHIFT and pressing TAB at any point will back up the client database by creating a copy of the database that
will only be accessed during database recovery.

Holding SHIFT and pressing ENTER at any point will bring up a password entry box. Upon entering the correct password,
the main database will be recovered using the backup databases.

