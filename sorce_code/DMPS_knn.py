#knn実行ファイル

#ライブラリの読み込み
import pandas as pd
import os
import datetime
import numpy as np
import tkinter as tk
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

#knn実行関数
def knn_judge(ndvi, fdi, setting_detail):
    #ログ出力
    log = setting_detail[17]
    start_time = datetime.datetime.now()
    log.insert(tk.END,"Start time : " + str(start_time)+"\n")
    log.see("end")
    #教師データの読み込み
    excel_path = setting_detail[18]
    if excel_path == "":
        log.insert(tk.END,"Please Select a teacher data" + str(start_time)+"\n")
        log.see("end")
    else:
        excel_file = pd.read_excel(excel_path)
        #データのコピー
        df_X = excel_file.copy()
        df_Y = excel_file.copy()

        df_X = df_X.drop('検出物質',axis=1)         #Excelデータから属性データのみを取り出す
        drop_idx = ['NDVI','FDI']#取得したExcelデータから目的変数のみを取り出す
        df_Y = df_Y.drop(drop_idx,axis=1)
        #オーバーサンプリング処理で教師データの増量
        sm = SMOTE(k_neighbors=5) 
        df_X, df_Y = sm.fit_resample(df_X, df_Y)
        #ログ出力
        log.insert(tk.END,"Complete over sampling.\n")
        log.see("end")
        
        result_data = []
        if setting_detail[13] == False:
            pass
        elif setting_detail[13] == True:
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
            log.insert(tk.END,"Complete standardization.\n")
            log.see("end")

        log.insert(tk.END,"Start Knn\n")
        log.see("end")
        model = KNeighborsClassifier(n_neighbors=7) #k-NNインスタンス
        model.fit(df_X, df_Y.values.ravel())
        for count_all in range(len(ndvi)):
            result_data_row = []
            for count in range(len(ndvi[count_all])):
                target = [[ndvi[count_all][count],fdi[count_all][count]]]
                target = pd.DataFrame(target,columns = ['NDVI','FDI'])
                target = target.fillna(0)
                # 構築したモデルから検出物を判定
                judge_data = model.predict(target)
                result_data_row.append(judge_data[0])
            result_data.append(result_data_row)

    #pickleで検出結果の保持
        with open(os.path.dirname(__file__) + "/pickle/judge.pickle", mode='wb') as f:
            pickle.dump(result_data, f)
    #log用
        string = setting_detail[12]
        with open(os.getcwd() + f"/pickle_log/{string}_" + start_time.strftime('%Y年%m月%d日%H時%M分%S秒') + ".pickle", mode='wb') as f:
            pickle.dump(result_data, f)

        end_time = datetime.datetime.now()
        log.insert(tk.END,"End time : " + str(end_time)+"\n")
        log.see("end")
        return result_data
