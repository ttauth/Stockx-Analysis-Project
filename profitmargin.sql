ALTER TABLE `StockX_Data`
MODIFY COLUMN `Sale Price` DECIMAL(10, 2),
MODIFY COLUMN `Retail Price` DECIMAL(10, 2),
MODIFY COLUMN `Profit` DECIMAL(10, 2),
MODIFY COLUMN `Profit Margin` DECIMAL(20, 10);
-- Recalculate Profit Margin values
UPDATE `StockX_Data`
SET 
    `Sale Price` = CAST(REPLACE(`Sale Price`, '$', '') AS DECIMAL(10, 2)),
    `Retail Price` = CAST(REPLACE(`Retail Price`, '$', '') AS DECIMAL(10, 2)),
    `Profit` = `Sale Price` - `Retail Price`,
    `Profit Margin` = CASE
        WHEN `Sale Price` > 0 THEN (`Profit` / `Sale Price`) * 100
        ELSE NULL
    END;

