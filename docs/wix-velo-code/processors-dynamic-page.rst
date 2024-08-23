Velo Code Used on Processors Dynamic Page
=============================================

Below is the velo code used on our dynamic Processors Page: https://www.sparkflows.io/processors?category=Data-Connectors

import wixData from 'wix-data';
import wixLocation from 'wix-location';

$w.onReady(() => {
    const query = wixLocation.query;
    showLoader();
    populateCategories()
        .then(() => {
            if (query.category) {
                selectCategory(query.category);
            } else {
                selectDefaultCategory();
            }
            $w('#subCategorySection').expand()
        })
        .finally(hideLoader);
});

let previousSelectedCategory = null;

const fetchDistinctCategories = () =>
    wixData.query("ProcessorsDynamicDatabase").distinct("category");

const fetchSubCategories = (category) =>
    wixData.query("ProcessorsDynamicDatabase")
          .eq("category", category)
          .find();

const fetchTableData = (subCategory) =>
    wixData.query("ProcessorsDynamicDatabase").eq("subCategory", subCategory).find();

function populateCategories() {
    return fetchDistinctCategories()
        .then((result) => {
            const categories = result.items.map((category, index) => ({ _id: String(index), category }));
            categories.sort((a, b) => {
                if (a.category === "Home") return -1;
                if (b.category === "Home") return 1;  
                return a.category.localeCompare(b.category);
            });
            $w("#categoryRepeater").data = categories;
        })
        .catch(console.error);
}

function selectCategory(category) {
    
    const categories = $w("#categoryRepeater").data;
    const categoryItem = categories.find(item => item.category === category);
    
    if (categoryItem) {
        $w("#categoryRepeater").forItems([categoryItem._id], ($item, itemData) => {
            handleCategoryClick($item, itemData);
        });
    }
}

function selectDefaultCategory() {
    const categories = $w("#categoryRepeater").data;
    if (categories.length > 0) {
        const defaultCategoryItem = categories[0];
        $w("#categoryRepeater").forItems([defaultCategoryItem._id], ($item, itemData) => {
            handleCategoryClick($item, itemData);
        });
    }
}

function handleCategoryClick($item, itemData) {
    showLoader();
    if (previousSelectedCategory) {
        previousSelectedCategory.html = `<span style="font-size: 16px; color: white;display: block; text-align: center">${previousSelectedCategory.text}</span>`;
    }
    $item("#categoryText").html = `<span style="font-size: 16px; color: #EF9010;display: block; text-align: center"><b><u>${itemData.category}</u></b></span>`;
    previousSelectedCategory = $item("#categoryText");

    clearSubCategories();

    populateSubCategories(itemData.category)
        .finally(hideLoader);
    wixLocation.queryParams.add({ category: itemData.category });
}

$w("#categoryRepeater").onItemReady(($item, itemData) => {
    $item("#categoryText").html = `<span style="font-size: 16px; color: white;display: block; text-align: center">${itemData.category}</span>`;
    
    $item("#categoryText").onClick(() => {
        handleCategoryClick($item, itemData);
    });
});

function clearSubCategories() {
    $w("#subCategoryRepeater").data = [];
}

function populateSubCategories(category) {
    return fetchSubCategories(category)
        .then((result) => {
           
            const subCategoriesMap = new Map();
            
            result.items.forEach((item) => {
                if (!subCategoriesMap.has(item.subCategory)) {
                    subCategoriesMap.set(item.subCategory, {
                        subCategory: item.subCategory,
                        icon: item.imageUrl,
                        tagline: item.subHeading
                    });
                }
            });

            const subCategories = Array.from(subCategoriesMap.values()).map((item, index) => ({
                _id: String(index),
                subCategory: item.subCategory,
                icon: item.icon,
                tagline: item.tagline
            }));
            
            subCategories.sort((a, b) => a.subCategory.localeCompare(b.subCategory));
            $w("#subCategoryRepeater").data = subCategories;
        })
        .catch(console.error);
}

$w("#subCategoryRepeater").onItemReady(($item, itemData) => {
    $item("#subCategoryText").text = itemData.subCategory;
    if (itemData.icon) {
        $item("#subCategoryIcon").src = itemData.icon;
        $item("#subCategoryIcon").expand(); 
    } else {
        $item("#subCategoryIcon").collapse(); 
    } 
    $item("#subCategoryTagline").text = itemData.tagline; 
    populateTable($item, itemData.subCategory);
});

function populateTable($item, subCategory) {
    showLoader();
    fetchTableData(subCategory)
        .then((results) => {
            const tableData = results.items.map((item, index) => ({
                _id: String(index),
                title: item.name,
                description: item.description,
                url: item.url,
                buttonText: item.cta
            }));
            
            const table = $item("#dataTable");
            if (table) {
                table.columns = [
                    { id: 'column1', dataPath: 'title', label: 'Title', type: 'string', width:170 },
                    { id: 'column2', dataPath: 'description', label: 'Description', type: 'string', width: 372 },
                    { id: 'column3', dataPath: 'buttonText', linkPath: "url", label: 'Links', type: 'string', width: 88 }
                ];
                table.rows = tableData;
            }
            
        })
        .catch(console.error)
        .finally(hideLoader);
}

function showLoader() {
    $w("#loader").show();
    $w('#loaderStrip').expand();
}

function hideLoader() {
    $w("#loader").hide();
    $w('#loaderStrip').collapse();
}
