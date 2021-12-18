-- FILE CONTAINING SQL QUERIES USED

-- q[0]: pnl
SELECT
    *
FROM
    (SELECT
        item,
        SUM(CASE WHEN period = "2017" THEN value ELSE 0 END) AS "2017",
        SUM(CASE WHEN period = "2018" THEN value ELSE 0 END) AS "2018",
        SUM(CASE WHEN period = "2019" THEN value ELSE 0 END) AS "2019",
        SUM(CASE WHEN period = "2020" THEN value ELSE 0 END) AS "2020",
        SUM(CASE WHEN period = "2021" THEN value ELSE 0 END) AS "2021"
    FROM
        pnl
    GROUP BY
        item
    HAVING
        ticker = ?
    ORDER BY
        item)
WHERE
    item="revenue" or item="ebitda";

-- q[1]: test
SELECT * FROM X;

-- q[2]: test
SELECT * FROM pnl WHERE ticker = ?;