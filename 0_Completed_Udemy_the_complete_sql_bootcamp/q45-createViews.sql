﻿CREATE VIEW customer_info AS 

SELECT first_name, last_name,email,address,phone FROM customer
JOIN address
ON customer.address_id = address.address_id;