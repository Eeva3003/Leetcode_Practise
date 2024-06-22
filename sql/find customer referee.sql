SELECT name
FROM Customer
WHERE COALESCE(referee_id,0) <> 2;

--here COALESCE is used to replace NULL values with zero before checking whether it is equal to 2 or not.
