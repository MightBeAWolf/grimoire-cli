
#### Example 1: Calculate the MD5 Checksum of a File

Arguments:
- `$1`: The file path for which the checksum is to be calculated.

```bash
md5sum $1
```

#### Example 2: Convert Spaces in Filenames to Underscores

Arguments:
- `$1`: Directory containing files to be renamed.

```bash
for file in $1/*; do mv "$file" `echo $file | tr ' ' '_'`; done
```

#### Example 3: Create a Backup of a Directory

Arguments:
- `$1`: Source directory.
- `$2`: Backup directory.

```bash
tar -czf $2/backup_$(date +%Y%m%d).tar.gz $1
```

#### Example 4: Display Lines Containing a Specific Pattern in a File

Arguments:
- `$1`: The pattern to search for.
- `$2`: The file to search in.

```bash
grep "$1" $2
```

#### Example 5: Convert a CSV File to JSON Format

Arguments:
- `$1`: The CSV file.
- `$2`: The JSON output file.

```bash
awk -F, '{print "{\""$1"\":\""$2"\", \""$3"\":\""$4"\"}"}' $1 > $2
```

#### Example 6: Send an Email Using `mailx`

Arguments:
- `$1`: Recipient's email address.
- `$2`: Subject of the email.
- `$3`: Body of the email.
- `$4`: Attachment file (optional).

```bash
echo "$3" | mailx -s "$2" -a "$4" $1
```

#### Example 7: Monitor a Log File in Real-Time

Arguments:
- `$1`: The log file to be monitored.

```bash
tail -f $1
```

#### Example 8: Compress a List of Files

Arguments:
- `$@`: Files to be compressed.

```bash
tar -czf compressed_files.tar.gz "$@"
```

