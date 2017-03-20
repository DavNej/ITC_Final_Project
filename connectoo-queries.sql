
-- ############################## Pictures BEGIN ##############################

-- Pics of Kid:
ALTER TABLE kid_photos ADD FOREIGN KEY (kid_id) REFERENCES kids(id); -- (DONE in local DB)
-- https://connectoo.co.il/uploads/kid_photos/{{kids.id}}/original/data.jpg

-- Pics of children in Kgarden
ALTER TABLE pictures ADD FOREIGN KEY (k_garden_id) REFERENCES k_gardens(id)
-- https://connectoo.co.il/uploads/pictures/{{pictures.id}}/original/data.jpg

-- Pics from attachments table (can't know where the pics come from... no link to other table)
select * from attachments;
--  https://connectoo.co.il/uploads/attachments/{{attachments.id}}/original/profile_pic.png
--  https://connectoo.co.il/uploads/attachments/{{attachments.id}}/original/data.jpg

-- ############################## Pictures END ##############################


-- ############################## Profile Pictures BEGIN ##############################

-- Profile pic of kid
-- https://connectoo.co.il/uploads/profile_pics/{{kids.id}}/square/data.jpg

-- Profile pic for users:
select * from users where picture_file_size is not null;
-- https://connectoo.co.il/uploads/user_picture/{{users.id}}/square/data.jpg

-- KGardens profile pics
select * from users where picture_file_size is not null;
-- https://connectoo.co.il/uploads/garden/{{garden.id}}/square/data.jpg

-- Contacts profile pics
select * from contacts where contact_pic_file_name = 'data';
-- https://connectoo.co.il/uploads/contact_pic/144/square/data.jpg

-- ############################## Profile Pictures END ##############################





-- kid information: MISSING ALOT OF COLUMNS LIKE K_GARDEN 
select first_name,address from kids where id = 30;


https://connectoo.co.il/uploads//bulletin_link/110/original/open-uri20161230-16605-175p3iv.jpg
https://connectoo.co.il/uploads//bulletin_link/30/original/data.jpg
