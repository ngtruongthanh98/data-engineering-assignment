import pyodbc
import boto3
import mysql.connector
import traceback
import re
import random

connection = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=data_eng;Trusted_Connection=yes;')
mssql_cursor = connection.cursor()

client = boto3.client('dynamodb', endpoint_url='http://localhost:8000')

mssql_cursor.execute("SELECT p.*, ps.name as SubcategoryName, pc.Name as CategoryName FROM data_eng.Production.Product p " \
"LEFT JOIN data_eng.Production.ProductSubcategory ps ON p.ProductSubcategoryID = ps.ProductSubcategoryID " \
"LEFT JOIN data_eng.Production.ProductCategory pc ON ps.ProductCategoryID = pc.ProductCategoryID")
mssql_columns = [column[0] for column in mssql_cursor.description]
print(mssql_columns)

items = []

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bq"
)

mysql_cursor = mydb.cursor()
mysql_query = "select pi.id ProductID, " \
    "sc.name SubcategoryName, " \
    "pi.image PartnerItemImage , " \
    "pi.images PartnerItemImages , " \
    "pi.active_images PartnerItemActiveImages , " \
    "pi.name ProductName , " \
    "pi.short_desc PartnerItemShortDesc , " \
    "pi.manufacturer_short_desc PartnerItemManufacturerShortDesc , " \
    "pi.desc PartnerItemDesc , " \
    "pi.manufacturer PartnerItemManufacturer , " \
    "pi.manufacturer_url PartnerItemManufacturerUrl , " \
    "pi.instruction_url PartnerItemInstructionUrl , " \
    "pi.instruction_video_url PartnerItemInstructionVideoUrl , " \
    "pi.limitations PartnerItemLimitations , " \
    "pi.monthly_cost PartnerItemMonthlyCost , " \
    "pi.for_sale PartnerItemForSale , " \
    "pi.is_available PartnerItemIsAvailable , " \
    "pi.meta_title PartnerItemMetaTitle , " \
    "pi.meta_desc PartnerItemMetaDesc , " \
    "pi.meta_keywords PartnerItemMetaKeywords , " \
    "pi.created PartnerItemCreated , " \
    "pi.cost_per_day PartnerItemCost_perDay , " \
    "pi.item_type PartnerItemItemType , " \
    "pi.qty PartnerItemQty , " \
    "pi.is_package PartnerItemIsPackage , " \
    "pi.package_item_ids PartnerItemPackageItemIds , " \
    "pi.is_identified PartnerItemIsIdentified , " \
    "pi.identify_item_id PartnerItemIdentifyItem_id , " \
    "pi.amazon_product_title PartnerItemAmazonProductTitle , " \
    "pi.manufacturer_description PartnerItemManufacturerDescription , " \
    "pi.manufacturer_images PartnerItemManufacturerImages , " \
    "pi.attributes PartnerItemAttributes , " \
    "pi.specifications PartnerItemSpecifications , " \
    "pi.style PartnerItemStyle , " \
    "pi.color_url PartnerItemColorUrl , " \
    "pi.color PartnerItemColor , " \
    "pi.sub_categories PartnerItemSubcategories , " \
    "di.image DefaultItemImage, " \
    "di.images DefaultItemImages, " \
    "di.name DefaultItemName, " \
    "di.short_desc DefaultItemShortDesc, " \
    "di.desc DefaultItemDesc, " \
    "di.url_name DefaultItemUrlName, " \
    "di.manufacturer DefaultItemManufacturer, " \
    "di.manufacturer_url DefaultItemManufacturerUrl, " \
    "di.instruction_pdf DefaultItemInstructionPdf, " \
    "di.limitations DefaultItemLimitations, " \
    "di.show_public DefaultItemShow_public, " \
    "di.is_monthly DefaultItemIs_monthly, " \
    "di.monthly_cost DefaultItemMonthlyCost, " \
    "di.for_sale DefaultItemForSale, " \
    "di.is_editable DefaultItemIsEditable, " \
    "di.is_available DefaultItemIsAvailable, " \
    "di.purchase_surcharge_percent DefaultItemPurchaseSurcharge_percent, " \
    "di.mandatory_delivery DefaultItemMandatoryDelivery, " \
    "di.meta_title DefaultItemMetaTitle, " \
    "di.meta_desc DefaultItemMetaDesc, " \
    "di.meta_keywords DefaultItemMetaKeywords, " \
    "di.created DefaultItemCreated, " \
    "di.modified DefaultItemModified, " \
    "di.cost_per_day DefaultItemCostPerDay, " \
    "di.cost_to_purchase DefaultItemCostToPurchase, " \
    "di.item_type DefaultItemItemType, " \
    "di.is_package DefaultItemIsPackage, " \
    "di.is_limit_inventory DefaultItemIsLimitInventory, " \
    "di.package_item_ids DefaultItemPackageItemIds, " \
    "di.is_identified DefaultItemIsIdentified, " \
    "di.amazon_product_id DefaultItemAmazonProductId, " \
    "di.is_show_specs DefaultItemIsShowSpecs, " \
    "di.amazon_product_title DefaultItemAmazonProductTitle, " \
    "di.asin DefaultItemAsin, " \
    "di.parent_asin DefaultItemParentAsin, " \
    "di.manufacturer_description DefaultItemManufacturerDescription, " \
    "di.manufacturer_images DefaultItemManufacturerImages, " \
    "di.attributes DefaultItemAttributes, " \
    "di.specifications DefaultItemSpecifications, " \
    "di.model_number DefaultItemModelNumber, " \
    "di.tab_description DefaultItemTabDescription, " \
    "di.manufacturer_date DefaultItemManufacturerDate, " \
    "it.request_parameters IdentityItemRequestParameters, " \
    "it.title IdentityItemTitle, " \
    "it.search_title IdentityItemSearchTitle, " \
    "it.title_excluding_variant_name IdentityItemTitleExcludingVariantName, " \
    "it.keywords IdentityItemKeywords, " \
    "it.keywords_list IdentityItemKeywordsList, " \
    "it.asin IdentityItemAsin, " \
    "it.parent_asin IdentityItemParentAsin, " \
    "it.link IdentityItemLink, " \
    "it.brand IdentityItemBrand, " \
    "it.variants IdentityItemVariants, " \
    "it.variant_asins_flat IdentityItemVariantAsinsFlat, " \
    "it.categories IdentityItemCategories, " \
    "it.description IdentityItemDescription, " \
    "it.rating IdentityItemRating, " \
    "it.rating_breakdown IdentityItemRatingBreakdown, " \
    "it.ratings_total IdentityItemRatingsTotal, " \
    "it.reviews_total IdentityItemReviewsTotal, " \
    "it.main_image IdentityItemMainImage, " \
    "it.images IdentityItemImages, " \
    "it.attributes IdentityItemAttributes, " \
    "it.specifications IdentityItemSpecifications, " \
    "it.specifications_flat IdentityItemSpecificationsFlat, " \
    "it.color IdentityItemColor, " \
    "it.material IdentityItemMaterial, " \
    "it.weight IdentityItemWeight, " \
    "it.dimensions IdentityItemDimensions, " \
    "it.model_number IdentityItemModelNumber, " \
    "it.is_generic IdentityItemIs_generic, " \
    "it.is_sub_category_banned IdentityItemIsSubCategoryBanned, " \
    "it.is_item_banned IdentityItemIsItemBanned, " \
    "it.is_suggested IdentityItemIsSuggested, " \
    "it.is_recommended IdentityItemIsRecommended, " \
    "it.search_keyword IdentityItemSearchKeyword, " \
    "it.recommended_price IdentityItemRecommendedPrice, " \
    "it.instructional_video_url IdentityItemInstructionalVideoUrl, " \
    "it.suggested_daily_price IdentityItemSuggestedDailyPrice, " \
    "it.suggested_monthly_price IdentityItemSuggestedMonthlyPrice, " \
    "it.is_set_price_directly IdentityItemIsSetPriceDirectly, " \
    "it.price_sub_category IdentityItemPriceSubCategory, " \
    "it.is_package IdentityItemIsPackage, " \
    "it.subcategories IdentityItemSubcategories, " \
    "it.is_non_generic IdentityItemIsNonGeneric, " \
    "it.source IdentityItemSource, " \
    "it.package_item_ids IdentityItemPackageItemIds, " \
    "it.created IdentityItemCreated, " \
    "it.modified IdentityItemModified, " \
    "it.is_hidden IdentityItemIs_hidden, " \
    "it.is_sub_category_hidden IdentityItemIsSubCategoryHidden, " \
    "it.is_carseat IdentityItemIsCarseat, " \
    "it.short_desc IdentityItemShortDesc, " \
    "it.most_specific_sub_category_id IdentityItemMostSpecificSubCategoryId, " \
    "it.suggested_purchase_price IdentityItemSuggestedPurchasePrice, " \
    "it.is_custom IdentityItemIsCustom, " \
    "it.for_sale IdentityItemForSale, " \
    "it.identified_count IdentityItemIdentifiedCount, " \
    "it.instruction_manual_url IdentityItemInstructionManualUrl, " \
    "it.price IdentityItemPrice, " \
    "it.price_currency IdentityItemPriceCurrency, " \
    "it.prices IdentityItemPrices " \
    "FROM partner_items pi " \
    "LEFT JOIN default_items di ON pi.default_item_id = di.id " \
    "LEFT JOIN identify_items it ON pi.identify_item_id = it.id " \
    "LEFT JOIN partner_categories_items pci ON pci.partner_item_id = pi.id " \
    "LEFT JOIN categories c ON pci.category_id = c.id " \
		"LEFT JOIN category_sub_categories csc on csc.category_id =c.id " \
    "LEFT JOIN sub_categories sc on csc.sub_category_id=sc.id " \
    "group by pi.id" \

mysql_cursor.execute(mysql_query)
products_data = mysql_cursor.fetchall()
product_columns = [column[0] for column in mysql_cursor.description]
print("🚀 ~ file: category_table.py ~ line 14 ~ mysql_columns", product_columns)

mysql_cursor.execute("SELECT distinct(sc.name) FROM category_sub_categories csc LEFT JOIN categories c ON csc.category_id = c.id LEFT JOIN sub_categories sc ON sc.id = csc.sub_category_id")
subcategories = mysql_cursor.fetchall()
subcategories = [sc[0] for sc in subcategories]

'''MSSQL PROCESSING'''
for row in mssql_cursor.fetchall():
    index = {
      "PutRequest": {
        "Item": {}
      }
    }
    # Add custom column here
    for i, column in enumerate(mssql_columns):
      if column == 'Name':
        index["PutRequest"]["Item"]["ProductName"] = {"S": str(row[i])}
      if column == 'SubcategoryName' and row[i] is None:
        index["PutRequest"]["Item"][column] = {'S': random.choice(subcategories)}
        
      elif row[i] is not None:
        if isinstance(row[i], bool):
          index["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          index["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
        else:
          index["PutRequest"]["Item"][column] = {"S": str(row[i])}
    items.append(index)

'''END OF MSSQL'''
for row in products_data:
    index = {
      "PutRequest": {
        "Item": {}
      }
    }
    # Add custom column here
    for i, column in enumerate(product_columns):
      if column == 'SubcategoryName' and row[i] is None:
        index["PutRequest"]["Item"][column] = {'S': random.choice(subcategories)}

      if row[i] is not None:
        if isinstance(row[i], bool):
          index["PutRequest"]["Item"][column] = {"BOOL": row[i]}
        elif isinstance(row[i], (int, float)):
          index["PutRequest"]["Item"][column] = {"N": f"{row[i]}"}
        else:
          index["PutRequest"]["Item"][column] = {"S": re.sub(re.compile('<.*?>'), '', str(row[i]))}
    items.append(index)

logf = open("logger.log", "w")

for item in items:
  print("~", item["PutRequest"]["Item"]["ProductID"]['N'])
  try:
    response = client.batch_write_item( 
      RequestItems={
        "Product": [item],
      }
    )
    if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
      logf.write("WARNING: {0}: {1}\n".format(str(item["PutRequest"]["Item"]), response))
  except BaseException as e:
    logf.write("ERROR: {0}: {1}\n".format(str(item["PutRequest"]["Item"]), str(e)))
    print(traceback.format_exc())


