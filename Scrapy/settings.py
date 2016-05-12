BOT_NAME = 'kitap'

SPIDER_MODULES = ['kitap.spiders']
NEWSPIDER_MODULE = 'kitap.spiders'
ITEM_PIPELINES = ['kitap.pipelines.JsonWithEncodingPipeline']
