/*
Create a Logging Table for Audit. To save records deleted or updated just in case you needed them back.
Also, we will create a trigger to save the records before they are deleted or updated.
*/

use sqlcleaningproject;

CREATE TABLE `nashvillehousing_log` (
    `UniqueID` int DEFAULT NULL,
    `ParcelID` varchar(255) DEFAULT NULL,
    `LandUse` varchar(255) DEFAULT NULL,
    `PropertyAddress` varchar(255) DEFAULT NULL,
    `SaleDate` date DEFAULT NULL,
    `SalePrice` int DEFAULT NULL,
    `LegalReference` varchar(255) DEFAULT NULL,
    `SoldAsVacant` varchar(10) DEFAULT NULL,
    `OwnerName` varchar(255) DEFAULT NULL,
    `OwnerAddress` varchar(255) DEFAULT NULL,
    `Acreage` float DEFAULT NULL,
    `TaxDistrict` text,
    `LandValue` int DEFAULT NULL,
    `BuildingValue` int DEFAULT NULL,
    `TotalValue` int DEFAULT NULL,
    `YearBuilt` int DEFAULT NULL,
    `Bedrooms` int DEFAULT NULL,
    `FullBath` int DEFAULT NULL,
    `HalfBath` int DEFAULT NULL,
    `PropertyAddressStreet` varchar(255) DEFAULT NULL,
    `PropertyAddressCity` varchar(255) DEFAULT NULL,
    `OwnerAddressStreet` varchar(255) DEFAULT NULL,
    `OwnerAddressCity` varchar(255) DEFAULT NULL,
    `OwnerAddressState` varchar(255) DEFAULT NULL,
    `operation_type` ENUM('insert', 'update', 'delete'),
    `operation_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

-------------------------------------------------------------------------------------------
-- Trigger for delete operation
-- Make sure the number of columns match the number of values 
-- I learnt that from past mistake i made

drop trigger if EXISTS after_record_delete; 
CREATE TRIGGER after_record_delete
AFTER DELETE ON nashvillehousing
FOR EACH ROW
BEGIN
    INSERT INTO nashvillehousing_log 
    (`UniqueID`, `ParcelID`, `LandUse`, `PropertyAddress`, `SaleDate`, `SalePrice`, `LegalReference`, `SoldAsVacant`, `OwnerName`,
     `OwnerAddress`, `Acreage`, `TaxDistrict`, `LandValue`, `BuildingValue`, `TotalValue`, `YearBuilt`, `Bedrooms`, `FullBath`, `HalfBath`, 
     `PropertyAddressStreet`, `PropertyAddressCity`, `OwnerAddressStreet`, `OwnerAddressCity`, `OwnerAddressState`, `operation_type`)
     VALUES
     (
     old.`UniqueID`, old.`ParcelID`, old.`LandUse`, old.`PropertyAddress`, old.`SaleDate`, old.`SalePrice`, old.`LegalReference`,
      old.`SoldAsVacant`, old.`OwnerName`, old.`OwnerAddress`, old.`Acreage`, old.`TaxDistrict`, old.`LandValue`, old.`BuildingValue`,
       old.`TotalValue`, old.`YearBuilt`, old.`Bedrooms`, old.`FullBath`, old.`HalfBath`, old.`PropertyAddressStreet`, old.`PropertyAddressCity`, 
       old.`OwnerAddressStreet`, old.`OwnerAddressCity`, old.`OwnerAddressState`, 'delete');
END;

------------------------------------------------------------------------------------------
-- Trigger for update operation
-- Make sure the number of columns match the number of values 
-- I learnt that from past mistake i made

drop trigger if EXISTS after_record_update; 

CREATE TRIGGER after_record_update
AFTER update ON nashvillehousing
FOR EACH ROW
BEGIN
    INSERT INTO nashvillehousing_log 
    (`UniqueID`, `ParcelID`, `LandUse`, `PropertyAddress`, `SaleDate`, `SalePrice`, `LegalReference`, `SoldAsVacant`, `OwnerName`,
     `OwnerAddress`, `Acreage`, `TaxDistrict`, `LandValue`, `BuildingValue`, `TotalValue`, `YearBuilt`, `Bedrooms`, `FullBath`, `HalfBath`, 
     `PropertyAddressStreet`, `PropertyAddressCity`, `OwnerAddressStreet`, `OwnerAddressCity`, `OwnerAddressState`, `operation_type`)
     VALUES
     (
     old.`UniqueID`, old.`ParcelID`, old.`LandUse`, old.`PropertyAddress`, old.`SaleDate`, old.`SalePrice`, old.`LegalReference`,
      old.`SoldAsVacant`, old.`OwnerName`, old.`OwnerAddress`, old.`Acreage`, old.`TaxDistrict`, old.`LandValue`, old.`BuildingValue`,
       old.`TotalValue`, old.`YearBuilt`, old.`Bedrooms`, old.`FullBath`, old.`HalfBath`, old.`PropertyAddressStreet`, old.`PropertyAddressCity`, 
       old.`OwnerAddressStreet`, old.`OwnerAddressCity`, old.`OwnerAddressState`, 'update');
END;


