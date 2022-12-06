import pandas as pd
import os
import datetime
import numpy as np
# 学習用データとテストデータに分けるためのモジュール（正解率を出すため）
from sklearn.model_selection import train_test_split
# k-近傍法（k-NN）
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle
import sys
sys.dont_write_bytecode = True
import warnings
warnings.simplefilter('ignore', UserWarning)
#オーバーサンプリング
from imblearn.over_sampling import SMOTE

def knn_judge(ndvi, fdi, setting_detail):

    start_time = datetime.datetime.now()
    print(start_time)

    excel_path = os.getcwd() + '\\teacherData\\teacherData_ver7.1_微修正版.xlsx'
    excel_file = pd.read_excel(excel_path)

    df_X = excel_file.copy()                    # データをコピーする。
    df_Y = excel_file.copy()

    df_X = df_X.drop('検出物質',axis=1)         #取得したExcelデータから属性データのみを取り出す
    drop_idx = ['NDVI','FDI']#取得したExcelデータから目的変数のみを取り出す
    df_Y = df_Y.drop(drop_idx,axis=1)

############################# over sampling ##################################
    sm = SMOTE(k_neighbors=5) 
    df_X, df_Y = sm.fit_resample(df_X, df_Y)
##############################################################################

    #X_train, X_test, y_train, y_test = train_test_split(df_X, df_Y, random_state=0) #ここから学習用データとテスト用データに分ける。random_stateは乱数を固定
    result_data = []
    if setting_detail[13].get() == False:
        pass
    elif setting_detail[13].get() == True:
        #標準化
        sc = StandardScaler()
        sc.fit(df_X)
        df_X = sc.transform(df_X)
        raw = len(ndvi)
        row = len(ndvi[0])
        
        ndvi = ndvi.flatten()
        fdi  = fdi.flatten()
        data = np.array([ndvi, fdi])
        data = sc.transform(data.T)
        ndvi = data.T[0].reshape(raw, row)
        fdi  = data.T[1].reshape(raw, row)
        data = None

    model = KNeighborsClassifier(n_neighbors=7) #k-NNインスタンス。今回は3個で多数決。3の値を変更して色々試すと〇
    #model.fit(X_train, y_train) #学習モデル構築。引数に訓練データの特徴量と、それに対応したラベル
    model.fit(df_X, df_Y.values.ravel())
    for count_all in range(len(ndvi)):
        result_data_row = []
        for count in range(len(ndvi[count_all])):
            target = [[ndvi[count_all][count],fdi[count_all][count]]]
            target = pd.DataFrame(target,columns = ['NDVI','FDI'])
            # 構築したモデルから検出物を判定
            judge_data = model.predict(target)
            result_data_row.append(judge_data[0])
        result_data.append(result_data_row)

#pickleで検出結果の保持
    with open(os.path.dirname(__file__) + "/pickle/judge.pickle", mode='wb') as f:
        pickle.dump(result_data, f)
#log用
    string = setting_detail[11]
    with open(os.getcwd() + f"/pickle_log/{string}_" + start_time.strftime('%Y年%m月%d日%H時%M分%S秒') + ".pickle", mode='wb') as f:
        pickle.dump(result_data, f)

    end_time = datetime.datetime.now()
    print("Judge End time : ",end_time)
    return result_data
