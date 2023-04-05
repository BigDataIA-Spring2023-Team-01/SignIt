import kaggle

kaggle.api.authenticate()

kaggle.api.dataset_download_files('risangbaskoro/wlasl-processed', path='data/kaggledataset/videos', unzip=True)

print("Nice")