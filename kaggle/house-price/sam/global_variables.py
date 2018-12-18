train_path = './input/train.csv'
test_path = './input/test.csv'

# Created lists of feature names for missing values
large_null_features = [
    'MiscFeature'
]
fill_mean_features = [
    'MasVnrArea', 
    'GarageYrBlt', 
    'LotFrontage',
    'BsmtFinSF1',
    'BsmtFinSF2',
    'BsmtFullBath',
    'BsmtHalfBath',
    'BsmtUnfSF',
    'GarageArea',
    'GarageCars',
    'TotalBsmtSF'
]
# this is only the test set at the minute, review the training set to see what can be switched
fill_most_common_cat_features = [
    'Exterior1st',
    'Exterior2nd',
    'Functional',
    'KitchenQual',
    'MSZoning',
    'SaleType',
    'Utilities' 
]
create_NA_cat_features = [
    'Alley',
    'PoolQC',
    'BsmtCond', 
    'BsmtFinType1', 
    'BsmtFinType2',
    'BsmtQual', 
    'BsmtExposure',
    'Fence',
    'FireplaceQu', 
    'GarageCond', 
    'GarageFinish', 
    'GarageQual',
    'GarageType'
]
create_none_cat_features = [
    'MasVnrType'
]