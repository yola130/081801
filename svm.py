{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "54392843-a2aa-4d9a-9cf1-ecfee93183f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Users\\13054\n",
      "当前工作目录: E:\\博士期间材料\\毕业论文材料\\python运行代码-第七波\\APP\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "current_path = os.getcwd()\n",
    "print(current_path)\n",
    "new_path = 'E:/博士期间材料/毕业论文材料/python运行代码-第七波/APP'\n",
    "os.chdir(new_path)\n",
    "print(\"当前工作目录: %s\" % os.getcwd())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5564175e-fcad-4ab7-9bd9-ec8f7d7d2a6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "648868f2-fcae-4834-b534-cdbce2eb58ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv(r'E:/博士期间材料/毕业论文材料/python运行代码-第七波/APP/081202model1.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5c301a86-970c-4e81-81ba-808b475aafe5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1965 entries, 0 to 1964\n",
      "Data columns (total 9 columns):\n",
      " #   Column       Non-Null Count  Dtype  \n",
      "---  ------       --------------  -----  \n",
      " 0   Age          1965 non-null   int64  \n",
      " 1   hospital     1965 non-null   int64  \n",
      " 2   Elevated RR  1965 non-null   int64  \n",
      " 3   Neutrophils  1965 non-null   float64\n",
      " 4   LDH          1965 non-null   float64\n",
      " 5   Glucose      1965 non-null   float64\n",
      " 6   ALB          1965 non-null   float64\n",
      " 7   BUN          1965 non-null   float64\n",
      " 8   outcome      1965 non-null   int64  \n",
      "dtypes: float64(5), int64(4)\n",
      "memory usage: 138.3 KB\n"
     ]
    }
   ],
   "source": [
    "data.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "97337a25-b4af-4b6d-85d4-9dc22e20f7dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Age</th>\n",
       "      <th>hospital</th>\n",
       "      <th>Elevated RR</th>\n",
       "      <th>Neutrophils</th>\n",
       "      <th>LDH</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>ALB</th>\n",
       "      <th>BUN</th>\n",
       "      <th>outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>58</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4.11</td>\n",
       "      <td>135.0000</td>\n",
       "      <td>13.90</td>\n",
       "      <td>34.1000</td>\n",
       "      <td>17.7</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>77</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4.98</td>\n",
       "      <td>304.6095</td>\n",
       "      <td>5.90</td>\n",
       "      <td>35.6806</td>\n",
       "      <td>4.3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>54</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>5.89</td>\n",
       "      <td>225.0000</td>\n",
       "      <td>6.00</td>\n",
       "      <td>39.0000</td>\n",
       "      <td>6.9</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>66</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3.69</td>\n",
       "      <td>342.0000</td>\n",
       "      <td>6.39</td>\n",
       "      <td>43.7000</td>\n",
       "      <td>4.1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>53</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>4.77</td>\n",
       "      <td>199.0000</td>\n",
       "      <td>6.50</td>\n",
       "      <td>43.8000</td>\n",
       "      <td>5.4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Age  hospital  Elevated RR  Neutrophils       LDH  Glucose      ALB   BUN  \\\n",
       "0   58         1            0         4.11  135.0000    13.90  34.1000  17.7   \n",
       "1   77         1            0         4.98  304.6095     5.90  35.6806   4.3   \n",
       "2   54         1            0         5.89  225.0000     6.00  39.0000   6.9   \n",
       "3   66         1            0         3.69  342.0000     6.39  43.7000   4.1   \n",
       "4   53         1            0         4.77  199.0000     6.50  43.8000   5.4   \n",
       "\n",
       "   outcome  \n",
       "0        0  \n",
       "1        0  \n",
       "2        0  \n",
       "3        0  \n",
       "4        0  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a087eb2e-b656-40e9-b69e-35a835149103",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   hospital  Elevated RR  outcome       Age  Neutrophils       LDH   Glucose  \\\n",
      "0         1            0        0 -0.950119    -0.450849 -0.853830  1.753478   \n",
      "1         1            0        0  0.413743    -0.209782  0.198258 -0.522807   \n",
      "2         1            0        0 -1.237248     0.042369 -0.295560 -0.494354   \n",
      "3         1            0        0 -0.375861    -0.567227  0.430191 -0.383385   \n",
      "4         1            0        0 -1.309030    -0.267971 -0.456838 -0.352086   \n",
      "\n",
      "        ALB       BUN  \n",
      "0 -0.250133  1.916395  \n",
      "1  0.036874 -0.562932  \n",
      "2  0.639615 -0.081869  \n",
      "3  1.493047 -0.599937  \n",
      "4  1.511205 -0.359405  \n"
     ]
    }
   ],
   "source": [
    "from sklearn.preprocessing import StandardScaler  \n",
    "import pandas as pd  \n",
    "  \n",
    "# 假设 data1 是你的原始 DataFrame，包含 'Gender', 'Sleep disorder', 'Age', 'BMI', 可能还有其他列  \n",
    "  \n",
    "# 分离出需要标准化的连续变量  \n",
    "continuous_features = ['Age', 'Neutrophils', 'LDH', 'Glucose', 'ALB', 'BUN']  \n",
    "X_continuous = data[continuous_features]  \n",
    "  \n",
    "# 对连续变量进行标准化  \n",
    "scaler = StandardScaler()  \n",
    "X_scaled = scaler.fit_transform(X_continuous)  \n",
    "  \n",
    "# 将标准化后的数据转换回 DataFrame，并保留原始的列名  \n",
    "X_scaled_df = pd.DataFrame(X_scaled, columns=continuous_features)  \n",
    "  \n",
    "# 将标准化后的连续变量 DataFrame 与原始 DataFrame 中的其他列合并  \n",
    "# 注意：这里我们使用 data1.drop(continuous_features, axis=1) 来删除原始 DataFrame 中的连续变量列  \n",
    "# 然后使用 pd.concat 将其与标准化后的连续变量 DataFrame 合并  \n",
    "data_scaled = pd.concat([data.drop(continuous_features, axis=1), X_scaled_df], axis=1)  \n",
    "  \n",
    "# 显示结果  \n",
    "print(data_scaled.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "04746cad-5fff-49d0-a59b-0b1f44870a41",
   "metadata": {},
   "outputs": [],
   "source": [
    "#拆分数据\n",
    "data1 = data[data['hospital'] == 1]\n",
    "data2 = data[data['hospital'] == 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0fd21a40-c911-4e1e-82a9-dc4fc3343538",
   "metadata": {},
   "outputs": [],
   "source": [
    "data1 = data1.drop(['hospital'], axis = 1)\n",
    "data2 = data2.drop(['hospital'], axis = 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4dd63395-fff2-4c5c-b4ae-9b179ae805b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "X = data1.drop('outcome', axis=1)\n",
    "y = data1['outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "99fa29a3-961f-4074-ac38-3fe92cc00388",
   "metadata": {},
   "outputs": [],
   "source": [
    "X_test = data2.drop('outcome', axis=1)\n",
    "y_test = data2['outcome']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fa95e955-dbab-464c-b41b-15db7be0b0ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 导入train_test_split函数，用于划分训练集和测试集\n",
    "from sklearn.model_selection import train_test_split\n",
    "# 拆分数据集  \n",
    "X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=99)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f7a50ad6-8bd9-4035-af55-69743ef51fa6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "outcome\n",
       "0    946\n",
       "1    134\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(y_train).value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "c3059ac9-7030-4f84-84f2-fd4686373129",
   "metadata": {},
   "outputs": [],
   "source": [
    "from imblearn.combine import SMOTEENN  \n",
    "# 定义SMOTE对象\n",
    "smote_enn = SMOTEENN(random_state=99)    \n",
    "# 对训练集进行过采样  \n",
    "X_train, y_train = smote_enn.fit_resample(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "8828d38e-bbde-4ba2-9e71-9fda6b5aa58c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "outcome\n",
       "1    871\n",
       "0    682\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.Series(y_train).value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1b428859-a3e0-4eaf-9995-075d945782d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# 导入准确率和分类报告指标\n",
    "from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, auc, f1_score, recall_score, confusion_matrix, ConfusionMatrixDisplay"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6a1ada09-a42f-42ff-a2d3-f84a3fde4e63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "SVM train set confusion matrix:\n",
      "[[640  42]\n",
      " [172 699]]\n",
      "SVM validation set confusion matrix:\n",
      "[[320  70]\n",
      " [ 14  60]]\n",
      "SVM test set confusion matrix:\n",
      "[[275  78]\n",
      " [ 18  50]]\n"
     ]
    },
    {
     "data": {
      "image/png": "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AQC/PCR7/KzIyEilp6dr9erVbutXr16tHj16BCgqAICnwgMdAILD+PHjddNNN6lz587q3r27nn/+ee3bt0+jRo0KdGiAz8rKyrR7927X67y8PG3ZskUJCQlq2bJlACMD/INL7+CxefPmaebMmTpw4IA6dOig2bNn64orrgh0WIDPPvjgA1155ZV11o8cOVI5OTkNHxDgZyR7AABCHOfsAQAIcSR7AABCHMkeAIAQR7IHACDEkewBAAhxJHsAAEIcyR4AgBBHsgcAIMSR7AEfTZ06VRdffLHr9S233KKhQ4c2eBzffvutLBaLtmzZctox5557rubMmePxMXNycnTWWWf5HJvFYtHKlSt9Pg6AM0OyR0i65ZZbZLFYZLFYFBERofPOO08TJ05UeXl5vb/3U0895fEtVj1J0ADgKx6Eg5D161//WgsXLtSxY8f00Ucf6fbbb1d5ebnmz59fZ+yxY8cUERHhl/e12Wx+OQ4A+AuVPUKW1WqVw+FQcnKyRowYoRtuuMHVSj7Rev/LX/6i8847T1arVYZhqKSkRHfeeaeaNWum+Ph4XXXVVfr888/djvv444/LbrcrLi5OGRkZOnr0qNv2k9v4tbW1mjFjhtq0aSOr1aqWLVtq+vTpkqSUlBRJUqdOnWSxWNSrVy/XfgsXLlS7du0UFRWlCy64QPPmzXN7n08//VSdOnVSVFSUOnfurM2bN3v9M5o1a5bS0tIUGxur5ORkjR49WmVlZXXGrVy5Uueff76ioqLUt29f5efnu23/xz/+ofT0dEVFRem8887TI488ourqaq/jAVA/SPYwjejoaB07dsz1evfu3XrllVf02muvudro11xzjQoLC/XWW28pNzdXl1xyiXr37q0ffvhBkvTKK6/o4Ycf1vTp07Vp0yY1b968ThI+2eTJkzVjxgw9+OCD2rFjh5YuXSq73S7peMKWpDVr1ujAgQP6+9//LklasGCBpkyZounTp2vnzp3KysrSgw8+qEWLFkmSysvLNXDgQLVt21a5ubmaOnWqJk6c6PXPJCwsTE8//bS2bdumRYsW6b333tOkSZPcxhw5ckTTp0/XokWL9PHHH8vpdOr66693bX/33Xd14403aty4cdqxY4eee+455eTkuL7QAPgFMIAQNHLkSGPIkCGu15988omRmJhoDB8+3DAMw3j44YeNiIgIo6ioyDXmX//6lxEfH28cPXrU7VitW7c2nnvuOcMwDKN79+7GqFGj3LZ37drV6Nix4ynf2+l0Glar1ViwYMEp48zLyzMkGZs3b3Zbn5ycbCxdutRt3WOPPWZ0797dMAzDeO6554yEhASjvLzctX3+/PmnPNb/atWqlTF79uzTbn/llVeMxMRE1+uFCxcakowNGza41u3cudOQZHzyySeGYRjG5ZdfbmRlZbkdZ/HixUbz5s1dryUZK1asOO37AqhfnLNHyPrnP/+pxo0bq7q6WseOHdOQIUP0zDPPuLa3atVKZ599tut1bm6uysrKlJiY6HaciooKffPNN5KknTt3atSoUW7bu3fvrvfff/+UMezcuVOVlZXq3bu3x3EfOnRI+fn5ysjI0B133OFaX11d7ZoPsHPnTnXs2FExMTFucXjr/fffV1ZWlnbs2CGn06nq6modPXpU5eXlio2NlSSFh4erc+fOrn0uuOACnXXWWdq5c6cuvfRS5ebmauPGjW6VfE1NjY4ePaojR464xQggMEj2CFlXXnml5s+fr4iICCUlJdWZgHcimZ1QW1ur5s2b64MPPqhzrDO9/Cw6OtrrfWprayUdb+V37drVbVujRo0kSYZhnFE8/2vv3r26+uqrNWrUKD322GNKSEjQunXrlJGR4Xa6Qzp+6dzJTqyrra3VI488omHDhtUZExUV5XOcAHxHskfIio2NVZs2bTwef8kll6iwsFDh4eE699xzTzmmXbt22rBhg26++WbXug0bNpz2mKmpqYqOjta//vUv3X777XW2R0ZGSjpeCZ9gt9t1zjnnaM+ePbrhhhtOedz27dtr8eLFqqiocH2h+Kk4TmXTpk2qrq7Wk08+qbCw49N3XnnllTrjqqurtWnTJl166aWSpF27dunHH3/UBRdcIOn4z23Xrl1e/awBNCySPfAfffr0Uffu3TV06FDNmDFDbdu21f79+/XWW29p6NCh6ty5s+69916NHDlSnTt31q9+9Su9/PLL2r59u84777xTHjMqKkr333+/Jk2apMjISF122WU6dOiQtm/froyMDDVr1kzR0dF655131KJFC0VFRclms2nq1KkaN26c4uPjNWDAAFVWVmrTpk0qLi7W+PHjNWLECE2ZMkUZGRn64x//qG+//VZ/+tOfvPq8rVu3VnV1tZ555hkNGjRIH3/8sZ599tk64yIiIjR27Fg9/fTTioiI0D333KNu3bq5kv9DDz2kgQMHKjk5Wddee63CwsL0xRdfaOvWrZo2bZr3/yEA+B2z8YH/sFgseuutt3TFFVfotttu0/nnn6/rr79e3377rWv2/HXXXaeHHnpI999/v9LT07V3717dfffdP3ncBx98UBMmTNBDDz2kdu3a6brrrlNRUZGk4+fDn376aT333HNKSkrSkCFDJEm33367XnjhBeXk5CgtLU09e/ZUTk6O61K9xo0b6x//+Id27NihTp06acqUKZoxY4ZXn/fiiy/WrFmzNGPGDHXo0EEvv/yysrOz64yLiYnR/fffrxEjRqh79+6Kjo7WsmXLXNv79++vf/7zn1q9erW6dOmibt26adasWWrVqpVX8QCoPxbDHyf/AADALxaVPQAAIY5kDwBAiCPZAwAQ4kj2AACEOJI9AAAhjmQPAECII9kDABDiSPYAAIQ4kj0AACGOZA8AQIgj2QMAEOL+H8fLZddoOonuAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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ADA5K8/GdyvZP/PMM26f8J577qlzMAAAwPfcSvazZs1y62Q2m41kDwA4L1n5FbduJfuCggJ/xwEAgF9ZuY1f59n41dXV2rVrl2pra30ZDwAAfnFqgp43S7DyONkfPXpUWVlZatSokTp06KC9e/dKOnmt/oknnvB5gAAAwDseJ/sHHnhAX375pT766CNFREQ4t/fr108rVqzwaXAAAPjKqTa+N0uw8vjWu1WrVmnFihXq3r27S0vj0ksv1TfffOPT4AAA8BUrT9DzuLI/cOCA4uPjT9teUVER1NczAAAwK4+TfdeuXfX22287108l+IULF6pHjx6+iwwAAB+y+WAJVh638XNycnTddddpx44dqq2t1dNPP63t27frs88+09q1a/0RIwAAXrPy43I9rux79uypTz/9VEePHlWbNm303nvvKSEhQZ999pkyMjL8ESMAAPBCnZ6Nn56ersWLF/s6FgAA/MbKr7itU7I/fvy4Vq5cqZ07d8pms6l9+/YaMmSIGjTgvToAgPOTldv4Hmfnbdu2aciQISouLtbFF18sSfr3v/+t5s2b64033lB6errPgwQAAHXn8TX72267TR06dNC+ffv0xRdf6IsvvlBhYaEuu+wy3X777f6IEQAAn7DiA3WkOlT2X375pTZt2qSmTZs6tzVt2lTTpk1T165dfRocAAC+YuU2vseV/cUXX6zvv//+tO0lJSW66KKLfBIUAAC+dmqCnjdLsHIr2TscDucyffp03XPPPXrllVe0b98+7du3T6+88oqys7M1Y8YMf8cLAAA85FYbv0mTJi7tC8MwNHz4cOc2wzAkSYMHD9bx48f9ECYAAN6xchvfrWT/4Ycf+jsOAAD8yttH3gZvqncz2ffq1cvfcQAAAD+p81Nwjh49qr1796q6utpl+2WXXeZ1UAAA+BqvuPXAgQMHNGjQIEVFRalDhw7q3LmzywIAwPnIm3vs63Kv/ccff6zBgwcrKSlJNptNq1atctk/evRo5zyCU0v37t1dxlRVVWn8+PGKi4tT48aNdeONN2rfvn0ef+0eJ/vs7GwdPnxYGzZsUGRkpN555x0tXrxYbdu21RtvvOFxAAAAmFFFRYU6duyouXPnnnXMddddp6KiIueyevVql/3Z2dlauXKlXnrpJa1bt07l5eUaNGiQx5PhPW7jr1mzRq+//rq6du2qkJAQpaSk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x9+TkJAQPfPMM9q2bZsWL16sNWvWaPLkyS5jjh49qmnTpmnx4sX69NNP5XA4dMsttzj3v/vuu/rtb3+re+65Rzt27NCCBQuUm5vr/IUGwHnAAExo1KhRxpAhQ5zr//znP41mzZoZw4cPNwzDMB555BGjYcOGRklJiXPMBx98YERHRxuVlZUu52rTpo2xYMECwzAMo0ePHsadd97psr9bt25Gx44dz/jZDofDCA8PNxYuXHjGOAsKCgxJxubNm122JycnG8uXL3fZ9uc//9no0aOHYRiGsWDBAiM2NtaoqKhw7p8/f/4Zz/VTKSkpxqxZs866/+WXXzaaNWvmXF+0aJEhydiwYYNz286dOw1Jxj//+U/DMAzj6quvNqZPn+5yniVLlhiJiYnOdUnGypUrz/q5APyLa/YwrbfeeksXXHCBamtrVVNToyFDhmjOnDnO/SkpKWrevLlzPT8/X+Xl5WrWrJnLeY4dO6ZvvvlGkrRz507deeedLvt79OihDz/88Iwx7Ny5U1VVVerbt6/bcR84cECFhYXKysrSmDFjnNtra2ud8wF27typjh07qlGjRi5xeOrDDz/U9OnTtWPHDjkcDtXW1qqyslIVFRVq3LixJKlBgwbq0qWL85hLLrlETZo00c6dO3XFFVcoPz9fGzdudKnkjx8/rsrKSh09etQlRgCBQbKHafXp00fz589Xw4YNlZSUdNoEvFPJ7JQTJ04oMTFRH3300WnnquvtZ5GRkR4fc+LECUknW/ndunVz2RcaGipJMgyjTvH81Hfffafrr79ed955p/785z8rNjZW69atU1ZWlsvlDunkrXM/d2rbiRMn9Oijj2rYsGGnjYmIiPA6TgDeI9nDtBo3bqyLLrrI7fGXX365iouL1aBBA7Vq1eqMY9q3b68NGzbo97//vXPbhg0bznrOtm3bKjIyUh988IFuu+220/aHhYVJOlkJn5KQkKALL7xQ3377rW699dYznvfSSy/VkiVLdOzYMecvFL8Ux5ls2rRJtbW1euqppxQScnL6zssvv3zauNraWm3atElXXHGFJGnXrl06cuSILrnkEkknv2+7du3y6HsNoH6R7IEf9evXTz169NDQoUM1Y8YMXXzxxdq/f79Wr16toUOHqkuXLrr33ns1atQodenSRVdddZWWLVum7du3q3Xr1mc8Z0REhO6//35NnjxZYWFhuvLKK3XgwAFt375dWVlZio+PV2RkpN555x21aNFCERERiomJ0dSpU3XPPfcoOjpamZmZqqqq0qZNm3T48GFNmDBBI0eO1JQpU5SVlaUHH3xQe/bs0V/+8hePvt42bdqotrZWc+bM0eDBg/Xpp5/q2WefPW1cw4YNNX78eD3zzDNq2LCh7r77bnXv3t2Z/B9++GENGjRIycnJuvnmmxUSEqKvvvpKW7du1eOPP+75PwQAn2M2PvAjm82m1atX65prrtEf/vAHtWvXTrfccov27NnjnD0/YsQIPfzww7r//vuVkZGh7777Tnfdddcvnvehhx7SxIkT9fDDD6t9+/YaMWKESkpKJJ28Hv7MM89owYIFSkpK0pAhQyRJt912m55//nnl5uYqPT1dvXr1Um5urvNWvQsuuEBvvvmmduzYoc6dO2vKlCmaMWOGR19vp06dNHPmTM2YMUNpaWlatmyZcnJyThvXqFEj3X///Ro5cqR69OihyMhIvfTSS879AwcO1FtvvaW8vDx17dpV3bt318yZM5WSkuJRPAD8x2b44uIfAAA4b1HZAwBgciR7AABMjmQPAIDJkewBADA5kj0AACZHsgcAwORI9gAAmBzJHgAAkyPZAwBgciR7AABMjmQPAIDJ/X8tl6ZnEM29ZwAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Training AUC: 0.9654, 95% CI: (0.9569, 0.9729)\n",
      "Validation AUC: 0.8680, 95% CI: (0.8172, 0.9115)\n",
      "Test AUC: 0.8525, 95% CI: (0.8047, 0.8944)\n",
      "Train set recall: 0.8025258323765786\n",
      "Validation set recall: 0.8108108108108109\n",
      "Test set recall: 0.7352941176470589\n",
      "Train set accuracy: 0.8622021893110109\n",
      "Validation set accuracy: 0.8189655172413793\n",
      "Test set accuracy: 0.7719714964370546\n",
      "Train set f1: 0.8672456575682381\n",
      "Validation set f1: 0.5882352941176471\n",
      "Test set f1: 0.5102040816326531\n",
      "Best cutoff value: 0.7413544851060714\n"
     ]
    }
   ],
   "source": [
    "from sklearn.svm import SVC  \n",
    "  \n",
    "# 创建SVM模型，这里使用RBF核（高斯核）  \n",
    "model_svm = SVC(kernel='linear', C=100, probability=True, random_state=99)  \n",
    "  \n",
    "# 训练模型  \n",
    "model_svm.fit(X_train, y_train)\n",
    "\n",
    "\n",
    "# 预测概率  \n",
    "y_train_svm_probs = model_svm.predict_proba(X_train)[:, 1]  \n",
    "y_val_svm_probs = model_svm.predict_proba(X_val)[:, 1]  \n",
    "y_test_svm_probs = model_svm.predict_proba(X_test)[:, 1]   \n",
    "\n",
    "\n",
    "# 初始化变量来存储最佳阈值和性能指标  \n",
    "best_threshold = None  \n",
    "best_j_index = -1  \n",
    "\n",
    "# 遍历可能的阈值（这里使用所有不同的预测概率作为阈值）  \n",
    "thresholds = np.unique(np.concatenate((y_train_svm_probs, y_val_svm_probs)))  \n",
    "for threshold in thresholds:  \n",
    "    # 计算validation集的混淆矩阵（仅用于选择最佳阈值）  \n",
    "    val_predictions = (y_val_svm_probs >= threshold).astype(int)  \n",
    "    tn, fp, fn, tp = confusion_matrix(y_val, val_predictions).ravel()  \n",
    "    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0  \n",
    "    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0  \n",
    "    j_index = sensitivity + specificity - 1  \n",
    "      \n",
    "    # 更新最佳阈值和约登指数  \n",
    "    if j_index > best_j_index:  \n",
    "        best_j_index = j_index  \n",
    "        best_threshold_svm = threshold\n",
    "\n",
    "  \n",
    "# 使用最佳阈值进行分类  \n",
    "y_train_svm_pred = (y_train_svm_probs >= best_threshold_svm).astype(int)  \n",
    "y_val_svm_pred = (y_val_svm_probs >= best_threshold_svm).astype(int)  \n",
    "y_test_svm_pred = (y_test_svm_probs >= best_threshold_svm).astype(int)  \n",
    "  \n",
    "# 混淆矩阵  \n",
    "train_svm_cm = confusion_matrix(y_train, y_train_svm_pred)  \n",
    "val_svm_cm = confusion_matrix(y_val, y_val_svm_pred)  \n",
    "# 注意：对于test集，我们通常不计算真实的混淆矩阵，因为没有真实的标签（或假设我们不知道它们）  \n",
    "# 但为了完整性，我们假设有标签并计算它  \n",
    "test_svm_cm = confusion_matrix(y_test, y_test_svm_pred)   \n",
    "\n",
    "# 绘制混淆矩阵图  \n",
    "disp_train_svm = ConfusionMatrixDisplay(confusion_matrix=train_svm_cm)\n",
    "disp_val_svm = ConfusionMatrixDisplay(confusion_matrix=val_svm_cm)\n",
    "disp_test_svm = ConfusionMatrixDisplay(confusion_matrix=test_svm_cm)\n",
    "  \n",
    "# 召回率、准确率  \n",
    "train_svm_recall = recall_score(y_train, y_train_svm_pred)  \n",
    "train_svm_accuracy = accuracy_score(y_train, y_train_svm_pred)  \n",
    "  \n",
    "val_svm_recall = recall_score(y_val, y_val_svm_pred)  \n",
    "val_svm_accuracy = accuracy_score(y_val, y_val_svm_pred)  \n",
    "  \n",
    "test_svm_recall = recall_score(y_test, y_test_svm_pred)  # 假设data2['target']是可用的  \n",
    "test_svm_accuracy = accuracy_score(y_test, y_test_svm_pred)  # 同样假设  \n",
    "\n",
    "# 计算F1分数  \n",
    "train_svm_f1 = f1_score(y_train, y_train_svm_pred)  \n",
    "val_svm_f1 = f1_score(y_val, y_val_svm_pred)  \n",
    "test_svm_f1 = f1_score(y_test, y_test_svm_pred)\n",
    "\n",
    "# 计算训练集AUC的95%置信区间  \n",
    "def auc_ci(y_train, y_train_svm_probs, n_bootstraps=1000, alpha=0.05):  \n",
    "    bootstrapped_scores = []  \n",
    "  \n",
    "    # 生成n_bootstraps个bootstrap样本，并计算每个样本的AUC  \n",
    "    for i in range(n_bootstraps):  \n",
    "        # 从原始样本中有放回地随机抽取样本  \n",
    "        indices = np.random.choice(len(y_train), len(y_train), replace=True)\n",
    "        y_train_svm_bootstrap = y_train.iloc[indices]\n",
    "        y_train_svm_probs_bootstrap = y_train_svm_probs[indices]\n",
    "    \n",
    "        score_svm = roc_auc_score(y_train_svm_bootstrap, y_train_svm_probs_bootstrap)  \n",
    "        bootstrapped_scores.append(score_svm)  \n",
    "  \n",
    "    # 计算置信区间  \n",
    "    bootstrapped_scores = np.array(bootstrapped_scores)  \n",
    "    lower = np.percentile(bootstrapped_scores, 100 * alpha / 2)  \n",
    "    upper = np.percentile(bootstrapped_scores, 100 * (1 - alpha / 2))  \n",
    "    return lower, upper  \n",
    "\n",
    "# 计算train集的AUC及其95%CI（虽然这通常不是基于阈值的）  \n",
    "train_svm_auc = roc_auc_score(y_train, y_train_svm_probs) \n",
    "train_svm_auc_ci = auc_ci(y_train, y_train_svm_probs) \n",
    "\n",
    "# 计算验证集AUC的95%置信区间  \n",
    "def auc_ci(y_val, y_val_svm_probs, n_bootstraps=1000, alpha=0.05):  \n",
    "    bootstrapped_scores = []  \n",
    "  \n",
    "    # 生成n_bootstraps个bootstrap样本，并计算每个样本的AUC  \n",
    "    for i in range(n_bootstraps):  \n",
    "        # 从原始样本中有放回地随机抽取样本  \n",
    "        indices = np.random.choice(len(y_val), len(y_val), replace=True)\n",
    "        y_val_svm_bootstrap = y_val.iloc[indices]\n",
    "        y_val_svm_probs_bootstrap = y_val_svm_probs[indices]\n",
    "    \n",
    "        score_svm = roc_auc_score(y_val_svm_bootstrap, y_val_svm_probs_bootstrap)  \n",
    "        bootstrapped_scores.append(score_svm)  \n",
    "  \n",
    "    # 计算置信区间  \n",
    "    bootstrapped_scores = np.array(bootstrapped_scores)  \n",
    "    lower = np.percentile(bootstrapped_scores, 100 * alpha / 2)  \n",
    "    upper = np.percentile(bootstrapped_scores, 100 * (1 - alpha / 2))  \n",
    "    return lower, upper \n",
    "\n",
    "# 计算validation集的AUC及其95%CI（虽然这通常不是基于阈值的） \n",
    "val_svm_auc = roc_auc_score(y_val, y_val_svm_probs)\n",
    "val_svm_auc_ci = auc_ci(y_val, y_val_svm_probs) \n",
    "\n",
    "\n",
    "# 计算测试集AUC的95%置信区间  \n",
    "def auc_ci(y_test, y_test_svm_probs, n_bootstraps=1000, alpha=0.05):  \n",
    "    bootstrapped_scores = []  \n",
    "  \n",
    "    # 生成n_bootstraps个bootstrap样本，并计算每个样本的AUC  \n",
    "    for i in range(n_bootstraps):  \n",
    "        # 从原始样本中有放回地随机抽取样本  \n",
    "        indices = np.random.choice(len(y_test), len(y_test), replace=True)\n",
    "        y_test_svm_bootstrap = y_test.iloc[indices]\n",
    "        y_test_svm_probs_bootstrap = y_test_svm_probs[indices]\n",
    "        \n",
    "        score_svm = roc_auc_score(y_test_svm_bootstrap, y_test_svm_probs_bootstrap)  \n",
    "        bootstrapped_scores.append(score_svm)  \n",
    "  \n",
    "    # 计算置信区间  \n",
    "    bootstrapped_scores = np.array(bootstrapped_scores)  \n",
    "    lower = np.percentile(bootstrapped_scores, 100 * alpha / 2)  \n",
    "    upper = np.percentile(bootstrapped_scores, 100 * (1 - alpha / 2))  \n",
    "    return lower, upper\n",
    "\n",
    "# 计算test集的AUC及其95%CI（虽然这通常不是基于阈值的） \n",
    "test_svm_auc = roc_auc_score(y_test, y_test_svm_probs)\n",
    "test_svm_auc_ci = auc_ci(y_test, y_test_svm_probs) \n",
    "\n",
    "print(\"SVM train set confusion matrix:\")  \n",
    "print(train_svm_cm)  \n",
    "print(\"SVM validation set confusion matrix:\")  \n",
    "print(val_svm_cm) \n",
    "print(\"SVM test set confusion matrix:\")  \n",
    "print(test_svm_cm)\n",
    "disp_train_svm.plot(cmap=plt.cm.Blues)\n",
    "disp_val_svm.plot(cmap=plt.cm.Blues)\n",
    "disp_test_svm.plot(cmap=plt.cm.Blues)\n",
    "\n",
    "plt.show()\n",
    "\n",
    "#输出AUC及其95%置信区间： \n",
    "print(f\"Training AUC: {train_svm_auc:.4f}, 95% CI: ({train_svm_auc_ci[0]:.4f}, {train_svm_auc_ci[1]:.4f})\")  \n",
    "print(f\"Validation AUC: {val_svm_auc:.4f}, 95% CI: ({val_svm_auc_ci[0]:.4f}, {val_svm_auc_ci[1]:.4f})\")  \n",
    "print(f\"Test AUC: {test_svm_auc:.4f}, 95% CI: ({test_svm_auc_ci[0]:.4f}, {test_svm_auc_ci[1]:.4f})\")\n",
    "\n",
    "\n",
    "print(f\"Train set recall: {train_svm_recall}\")  \n",
    "print(f\"Validation set recall: {val_svm_recall}\") \n",
    "print(f\"Test set recall: {test_svm_recall}\")\n",
    "\n",
    "print(f\"Train set accuracy: {train_svm_accuracy}\")   \n",
    "print(f\"Validation set accuracy: {val_svm_accuracy}\")   \n",
    "print(f\"Test set accuracy: {test_svm_accuracy}\")  \n",
    "\n",
    "print(f\"Train set f1: {train_svm_f1}\")  \n",
    "print(f\"Validation set f1: {val_svm_f1}\")  \n",
    "print(f\"Test set f1: {test_svm_f1}\")\n",
    "\n",
    "print(f\"Best cutoff value: {best_threshold_svm}\")  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "50fd3c08-dc71-4f2f-b41d-9cb6f455ee7b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['SVM.pkl']"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "# 保存模型\n",
    "joblib.dump(model_svm , 'SVM.pkl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6cbd4a94-a4f3-4d9f-81ac-c7e1a33ad215",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-08-18 20:02:51.099 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run D:\\download\\anaconda\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import shap\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Load the model\n",
    "model = joblib.load('SVM.pkl')\n",
    "\n",
    "# Define feature names\n",
    "feature_names = [\"Age\", \"Elevated_RR\", \"Neutrophils\", \"LDH\", \"Glucose\", \"ALB\", \"BUN\"]\n",
    "\n",
    "# Streamlit user interface\n",
    "st.title(\"A calculation tool for predicting in-hospital mortality in patients with COVID-19\")\n",
    "\n",
    "# age: numerical input\n",
    "Age = st.number_input(\"Age:\", min_value=1, max_value=120, value=70)\n",
    "\n",
    "# Elevated RR: categorical selection\n",
    "Elevated_RR = st.selectbox(\"Elevated_RR:\", options=[0, 1], format_func=lambda x: 'Normal (0)' if x == 0 else 'Elevated (1)')\n",
    "\n",
    "# Neutrophils: numerical input\n",
    "Neutrophils = st.number_input(\"Neutrophils:\", min_value=0, max_value=50, value=6)\n",
    "\n",
    "# LDH: numerical input\n",
    "LDH = st.number_input(\"LDH:\", min_value=50, max_value=4000, value=270)\n",
    "\n",
    "# Glucose: numerical input\n",
    "Glucose = st.number_input(\"Glucose:\", min_value=1, max_value=40, value=8)\n",
    "\n",
    "# ALB: numerical input\n",
    "ALB = st.number_input(\"ALB:\", min_value=0, max_value=100, value=35)\n",
    "\n",
    "# BUN: numerical input\n",
    "BUN = st.number_input(\"BUN:\", min_value=0, max_value=100, value=7)\n",
    "\n",
    "# Process inputs and make predictions\n",
    "feature_values = [Age, Elevated_RR, Neutrophils, LDH, Glucose, ALB, BUN]\n",
    "features = np.array([feature_values])\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    # Predict probabilities\n",
    "    predicted_proba = model.predict_proba(features)[0]\n",
    "    \n",
    "    # 根据预测概率的最高值来确定预测类别（但这里我们直接根据概率阈值判断）  \n",
    "    high_risk_threshold = 0.74  # 74% 的阈值  \n",
    "    if predicted_proba[1] > high_risk_threshold:  # 假设模型输出的第二个概率是高风险类的概率  \n",
    "        predicted_class = 1  # 高风险  \n",
    "    else:  \n",
    "        predicted_class = 0  # 低风险\n",
    "\n",
    "    probability = predicted_proba * 100\n",
    "\n",
    "     # 显示预测结果  \n",
    "    st.write(f\"**Predicted Class (Based on Probability Threshold)**: {'High Risk' if predicted_class == 1 else 'Low Risk'}\")  \n",
    "    st.write(f\"**Prediction Probabilities**: {probability}\")  \n",
    "\n",
    "\n",
    "    if predicted_class == 1:\n",
    "        advice = (\n",
    "            f\"High Risk. \"\n",
    "            f\"Based on the model, predicted that the probability of COVID-19 mortality is {probability:.1f}%. \"\n",
    "        )\n",
    "    else:\n",
    "        advice = (\n",
    "            f\"Low Risk. \"\n",
    "            f\"Based on the model, predicted that the probability of COVID-19 mortality is {probability:.1f}%. \"\n",
    "        )\n",
    "\n",
    "    st.write(advice)\n",
    "\n",
    "    # Calculate SHAP values and display force plot\n",
    "    explainer = shap.TreeExplainer(model)\n",
    "    shap_values = explainer.shap_values(pd.DataFrame([feature_values], columns=feature_names))\n",
    "\n",
    "    shap.force_plot(explainer.expected_value, shap_values[0], pd.DataFrame([feature_values], columns=feature_names), matplotlib=True)\n",
    "    plt.savefig(\"shap_force_plot.png\", bbox_inches='tight', dpi=1200)\n",
    "\n",
    "    st.image(\"shap_force_plot.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2000882-1bb8-4958-a380-fdbea5050a5b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
