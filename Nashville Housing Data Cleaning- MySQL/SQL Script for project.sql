/*
Cleaning data in sql queries
*/

use sqlcleaningproject;

select * from nashvillehousing;

-------------------------------------------------------------------

-- Populate Property Address Data

-- check records where PropertyAddress is NULL

select * from nashvillehousing where propertyaddress is null;

-- group by ParcelID and concatenate PropertyAddresses with group_concat() just to get a glimpse

select parcelid, GROUP_CONCAT(propertyaddress)
from nashvillehousing
    -- where  propertyaddress is null
GROUP BY
    parcelid
    -- having GROUP_CONCAT(propertyaddress) is NULL
ORDER BY parcelid
limit 1000;

-- check records with duplicate ParcelID

select *
from nashvillehousing
where
    parcelid in (
        select parcelid
        from nashvillehousing
        group by
            parcelid
        having
            count(parcelid) > 1
    );
-- and propertyaddress is null;

update nashvillehousing t1
inner join (
    select parcelid, max(propertyaddress) as maxpropertyaddress
    from nashvillehousing
    group by
        parcelid
    having
        count(parcelid) > 1
) t2 on t1.parcelid = t2.parcelid
set
    t1.propertyaddress = t2.maxpropertyaddress;

------------------------------------------------------------

-- Splitting Address into individual columns (Street, City, State)

select `PropertyAddress` from nashvillehousing;

-- Extract street and city from PropertyAddress
select SUBSTRING_INDEX(propertyaddress, ',', 1) as street, SUBSTRING_INDEX(propertyaddress, ',', -1) as city
from nashvillehousing;

alter table nashvillehousing
add column PropertyAddressStreet VARCHAR(255);

update nashvillehousing
set
    PropertyAddressStreet = SUBSTRING_INDEX(propertyaddress, ',', 1);

alter table nashvillehousing
add column PropertyAddressCity VARCHAR(255);

update nashvillehousing
set
    PropertyAddressCity = SUBSTRING_INDEX(propertyaddress, ',', -1);

select
    propertyaddress,
    propertyaddressstreet,
    propertyaddresscity
from nashvillehousing;

-- Extract street ,city, State from OwnerAddress
select SUBSTRING_INDEX(owneraddress, ',', 1) as street, SUBSTRING_INDEX(
        SUBSTRING_INDEX(owneraddress, ',', 2), ',', -1
    ) as city, SUBSTRING_INDEX(owneraddress, ',', -1) as state
from nashvillehousing;

alter table nashvillehousing
add column OwnerAddressStreet VARCHAR(255);

update nashvillehousing
set
    OwnerAddressStreet = SUBSTRING_INDEX(Owneraddress, ',', 1);

alter table nashvillehousing
add column OwnerAddressCity VARCHAR(255);

update nashvillehousing
set
    OwnerAddressCity = SUBSTRING_INDEX(
        SUBSTRING_INDEX(owneraddress, ',', 2),
        ',',
        -1
    );

alter table nashvillehousing
add column OwnerAddressState VARCHAR(255);

update nashvillehousing
set
    OwnerAddressState = SUBSTRING_INDEX(OwnerAddress, ',', -1);

select * from nashvillehousing;

----------------------------------------------------------------

-- Change Y and N to Yes and No in "Sold as Vacant" field

select DISTINCT soldasvacant from nashvillehousing;

select soldasvacant, count(`SoldAsVacant`)
from nashvillehousing
GROUP BY
    `SoldAsVacant`
ORDER BY 2;

select
    soldasvacant,
    case
        when soldasvacant = 'Y' then 'Yes'
        when soldasvacant = 'N' then 'No'
        else soldasvacant
    END
from nashvillehousing;

update nashvillehousing
set
    soldasvacant = case
        when soldasvacant = 'Y' then 'Yes'
        when soldasvacant = 'N' then 'No'
        else soldasvacant
    END;

----------------------------------------------------------------

-- Remove Duplicates

-- Check how many duplicate records are there

WITH RowNumCTE as (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY `ParcelID`, `PropertyAddress`, `SalePrice`, `SaleDate`, `LegalReference` ORDER BY uniqueid) row_num
    FROM nashvillehousing
)
select * from RowNumCTE 
where row_num > 1;

-- Delete the duplicate records

-- MySQL refused the delete operation... 

--  I found out why it didn't work, i needed to edit the triggers because 
-- i made a simple mistake where the number of columns didn't match the number of values so any delete operation
-- or update operations failed.

WITH RowNumCTE as (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY `ParcelID`, `PropertyAddress`, `SalePrice`, `SaleDate`, `LegalReference` ORDER BY uniqueid) row_num
    FROM nashvillehousing
) 
DELETE from nashvillehousing
where `UniqueID` in (select `UniqueID` from RowNumCTE where row_num > 1);

------------------------------------------------------------------------------

-- Delete Unused Columns

Select * From NashvilleHousing;


ALTER TABLE NashvilleHousing
DROP COLUMN OwnerAddress,
DROP COLUMN TaxDistrict,
DROP COLUMN PropertyAddress;




