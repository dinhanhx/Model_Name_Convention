# Model name convention

## Format

`<host>-<gpu config>-<core model name>-<internet source name>-<if modified use dax>-<timestamp>`

Explanation of tags:
- `host`: where gives gpus
- `gpu config`: `x` `gpu name` `y` GiB
- `core model name`: name of the largest model or name of the most important model
- `internet source`: name that can be searched easily on the internet to find `core model name` 
- `dax`: to indicate that I (Vu Dinh Anh) have modified model or hyper-parameters. If there is no, it means that I used exact model or hyper-parameters.
- `timestamp`: year, month, day, hour, minute ~ `YY_MM_DD_HH_mm`

Rule: if there is a dash in a tag, replace it by underscore.

## Example

`ICT6-1_K80_12GiB-UNITER-vladsandulescu-dax-2021_04_30_09_39`

This means that on ict 6, with 1 NVIDIA K80 12 GiB, UNITER model from vladsandulescu has been modified to train on 2021/04/30 at 09:39.

## Parser

Split by dash to get the tag information.

# Model reproduce instruction file

## File name

Follow `# Model name convention`. File extension: `.md`.

## File content

Detailed instruction to reproduce model from setup to train the model as well as expected outcome.

## Example 

Filename: `ICT6-1_K80_12GiB-UNITER-vladsandulescu-dax-2021_04_30_09_39.md`

Content:

```markdown
# I install like this

# Then I run like this

# Then I get these results

# Then I conclude like this
```

