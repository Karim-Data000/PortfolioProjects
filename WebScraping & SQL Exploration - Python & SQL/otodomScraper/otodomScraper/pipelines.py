# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re

class OtodomscraperPipeline:
    
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        field_names = adapter.field_names()
        
        # # converting rent string to number
        # rent_string = adapter.get('rent')
        # rent_string_split = rent_string.split(' ')
        # adapter['rent'] = rent_string_split[0]
        
        # converting rooms string to number
        rooms_string = item['rooms']
        try:
            item['rooms'] = int(rooms_string)
        except :
            item['rooms'] = None
        
        # converting price string to number
        price_string = item['price']
        if price_string:
            price_string_split = price_string.split(' ')
            final_price_string = "".join(price_string_split[:-1])
            final_price_string = final_price_string.replace(',', '.')
            item['price'] = float(final_price_string)
        else:
            item['price'] = 'Ask for price'            
        
        # converting price_per_m2 string to number
        price_per_m2_string = item['price_per_m2']
        if price_per_m2_string:
            price_per_m2_string_split = price_per_m2_string.split(' ')
            final_price_per_m2_string = "".join(price_per_m2_string_split[:-1])
            final_price_per_m2_string = final_price_per_m2_string.replace(',', '.')
            item['price_per_m2'] = float(final_price_per_m2_string)
        else:
            item['price_per_m2'] = 'Ask for price'


        # # converting Deposit string to number
        # Deposit_string = adapter.get('deposit')
        # Deposit_string_split = Deposit_string.split(' ')
        # final_Deposit_string = "".join(Deposit_string_split[:-1])
        # adapter['deposit'] = float(final_Deposit_string)
        
       
       
        #    clean listing description field from special characters
        
        def clean_description(text):
            # List of substrings to remove
            substrings_to_remove = ['\r\n', '\xa0', '+\xa0']
            
            # Additional cleaning: strip extra whitespace
            text = ' '.join(text)
            
            for substring in substrings_to_remove:
                text = text.replace(substring, ' ')
                        
            return text

        # Clean the listing_description field
        if 'listing_description' in item:
            item['listing_description'] = clean_description(item['listing_description'])

        
         
        # extract area from either the title or the listing description
        pattern = r'(\d\d+(?:[\.,]\d+)?)\s*(m2|sqm|m^2|m[\.\s]|m²)'

        # Function to extract area from a given text
        def extract_area(text):
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)
            return None


        # Check and extract area from listing_description
        if 'listing_description' in item and item['listing_description'] :
            area = extract_area(item['listing_description'])
            if area:
                item['area'] = area

        # Check and extract area from title if not found in listing_description
        if 'title' in item and item['title'] and len(item['area'])==0:
            area = extract_area(item['title'])
            if area:
                item['area'] = area
                
        # extract the number from the area string
        value = item['area']
        if 'sqm' in value:
            value = value.split('sqm')
            value = value[0].replace(',', '.')
            # value = '.'.join(value)
            item['area'] = float(value)
        elif 'm' in value:
            value = value.split('m')
            value = value[0].replace(',', '.')
            # value = '.'.join(value)
            item['area'] = float(value)

        
        # #  extract date from available_from date
    
        # date_pattern = r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}'
        
        # def extract_date(values):
        #     for value in values:
        #         if re.match(date_pattern, value):
        #             return value
        #     return 'contact for details'

        # # Extract date from available_from field
        # if 'available_from' in item:
        #     date = extract_date(item['available_from'])
        #     if date:
        #         item['available_from'] = date
        
        
        #  extract rent from rent field list
    
        rent_pattern = r'(\d\d+(?:[\.,\s]\d+)?)\s*'
        
        def extract_rent(values):
            for value in values:
                if re.match(rent_pattern, value):
                    value = value.split(" ")[:-1]
                    value = "".join(value)
                    value = value.replace(',', '.')
                    return float(value)
            return None

        # Extract rent from rent field or from balcony_garden field if it didn't exist in rent
        if 'rent' in item:
            rent1 = extract_rent(item['rent'])
            rent2 = extract_rent(item['balcony_garden'])
            if rent1:
                item['rent'] = rent1
            elif rent2:
                item['rent'] = rent2
            else:
                item['rent'] = 'contact for details'
                
                
        
        
        
        return item
