---
title: Search bar
tx_slug: documentation_how-to_search
---

# Search bar

QField is equipped with a search bar that allows you to:

- search for features within a project's vector layers
- [navigate to specified coordinates](../navigation-and-positioning/navigation.md#setting-a-destination-point)
- locate spatial bookmarks
- and calculate expressions

See [here](../../fieldwork/qfield-interface/search.md) how to use the search bar in QField

## Configure vector layers search in QGIS
:material-monitor: Desktop preparation

By default, all vector layers are searchable. To exclude specific layers from search queries:

!!! Workflow

    1. Open your project in QGIS.
    2. Navigate to _Project > Properties... > Data Sources_.
    !![Data Sources](../../assets/images/hiding-legend-nodes.png)
    3. Locate the layer capabilities table and uncheck the **Searchable** checkbox for any layers you wish to exclude.
    [Source configuration](../project-setup/data_source_and_project_paths.md#data-source-configuration)
