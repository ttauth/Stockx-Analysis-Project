SELECT *, `Sale Price` - `Retail Price` AS `Profit`
FROM `StockX_Data`
ORDER BY `Profit` DESC
LIMIT 100;
