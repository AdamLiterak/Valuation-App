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

-- q[1]: getting data for pandas DF PNL
SELECT * FROM financials WHERE (ticker like ?) AND (type like ?) AND (period > ?);

-- q[2]: finding MAX period available for the ticker in the db
SELECT MAX(period) FROM financials WHERE (ticker like ?) AND (type like ?);

-- q[3]: saving assumptions into the db
INSERT INTO assumptions (ticker, period, item, value) VALUEs (?,?,?,?);

-- junk trial
SELECT * FROM pnl LEFT JOIN ordered ON pnl.item=ordered.item WHERE pnl.type like "PNL" AND period>2018;


-- temporary 5
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
        (SELECT * FROM pnl LEFT JOIN ordered ON pnl.item = ordered.item ORDER BY ordered.ordered ASC)
    GROUP BY
        item
    HAVING
        ticker = ?
    ORDER BY
        item)
WHERE
    item="revenue" or item="ebitda";

