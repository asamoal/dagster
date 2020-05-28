# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestAssetAwareEventLog.test_get_all_asset_keys[in_memory_instance_in_process_env] 1'] = {
    'assetsOrError': {
        '__typename': 'AssetConnection',
        'nodes': [
            {
                'key': 'c'
            },
            {
                'key': 'b'
            },
            {
                'key': 'a'
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_materialization[in_memory_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'materialization': {
                        'label': 'a'
                    }
                }
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_all_asset_keys[asset_aware_instance_in_process_env] 1'] = {
    'assetsOrError': {
        '__typename': 'AssetConnection',
        'nodes': [
            {
                'key': 'a'
            },
            {
                'key': 'b'
            },
            {
                'key': 'c'
            }
        ]
    }
}

snapshots['TestAssetAwareEventLog.test_get_asset_key_materialization[asset_aware_instance_in_process_env] 1'] = {
    'assetOrError': {
        'assetMaterializations': [
            {
                'materializationEvent': {
                    'materialization': {
                        'label': 'a'
                    }
                }
            }
        ]
    }
}
