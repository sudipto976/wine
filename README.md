create env

```bash
conda create -n wineq python=3.8 -y
```

activate env

```bash
conda activate wineq
```

create req file

install req

```bash
pip install -r requirement.txt
```

```bash
git init
```

```bash
dvc init
```

```bash
dvc add data_given/winequality.csv
```

```bash
git add .
```

```bash
git commit -m "first commit"
```

```bash
git push origin main
```

mlflow server command -

mlflow server \
--backend-store-uri sqlite:///mlflow.db
--default-artifact-root ./artifacts
--host 0.0.0.0 -p 1234
