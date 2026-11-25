# Write your MySQL query statement below
WITH cte AS 
    (SELECT book_id, 
    COUNT(borrower_name) as current_borrowers
    FROM borrowing_records
    WHERE return_date IS NULL
    GROUP BY book_id)
SELECT c.book_id, c.title, c.author ,c.genre, c.publication_year, cte.current_borrowers
FROM library_books c
JOIN cte
ON c.book_id = cte.book_id
WHERE c.total_copies = cte.current_borrowers
ORDER BY cte.current_borrowers DESC, c.title ASC ;
