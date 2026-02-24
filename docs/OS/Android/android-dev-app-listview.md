# \[Android\] ListView

__ListView__ dùng để hiển thị danh sách các phần tử trong ứng dụng.

## UI

Khai báo trên giao diện

```xml
<ListView
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:id="@+id/listview">
</ListView>
```

## Khởi tạo 

### Set ArrayAdapter

- Tạo chuỗi _string_ `String[] array_listview`
- Tạo `ArrayList<String>` từ chuỗi _string_
- Tạo `ArrayAdapter<String>`
    - __Context__ được đặt bằng context của ứng dụng
    - Chọn __Layout__
        - Layout chọn trong `simple_list_item_1`,`simple_list_item_2`, ... được khai báo trong API
    - Cuối cùng đưa vào __ArrayList__ là tài nguyên cho __Adapter__

=== "Java"
    ```java title="Code Mẫu"
    String[] array_listview = {"Apple", "Banana", "Cherry"};
    ArrayList<String> arrayList = new ArrayList<String>(Arrays.asList(array_listview));
    ArrayAdapter<String> adapter = new ArrayAdapter<>(
        this,
        android.R.layout.simple_list_item_1,
        arrayList
    );

    ListView listView = findViewById(R.id.listview);
    listView.setAdapter(adapter);
    ```
=== "Kotlin"
    ```kotlin title="Code Mẫu"
    val arrayAdapter: ArrayAdapter<*>
    val users = arrayOf("Apple", "Banana", "Cherry")

    // access the listView from xml file
    listView = findViewById(R.id.user_list)
    arrayAdapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, users)
    listView.adapter = arrayAdapter
    ```

## Custom ListView

__Custom ListView__ là cách thay đổi thành phần của từng phần tử trong __ListView__, biến danh sách trở thành một danh sách mới tuỳ chỉnh thú vị hơn. Trước tiên làm ví dụ đơn giản làm ví dụ, một __ListView__ với _tiêu đề_ và _chú thích_.

<figure markdown="span">
    ![alt text](img/android-dev-app-listview-custom-0.png)
    <figcaption>ListView example</figcaption>
</figure>

### CustomAdapter

Đàu tiên biết rằng, để một ListView tải ra một danh sách cần có một __ArrayAdapter__, điều này lúc đầu khá phiền phức nhưng sau đó mình mới hiểu nó có tác dụng gì. Để tạo một danh sách phần tử có thể sửa đổi cho __ListView__ thì
Đàu tiên cần tạo một _class_ kế thừa từ __ArrayAdapter__ và được phát triển từ __View.OnClickListener__. Trong đó có hai hàm dùng để __Override__.

```puml
@startuml
class CustomAdapter extends ArrayAdapter
class CustomAdapter implements OnClickListener
@enduml
```
Phần mã khởi tạo như này:

=== "Java"
    ```java
    public class CustomAdapter extends ArrayAdapter<Pair<String, String>> implements View.OnClickListener {

        @Override
        public void onClick(View view) {
            // Code
        }

        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            // Code
        }
    }
    ```
=== "Kotlin"
    TO_DO

Sau đó thì bắt đầu tạo các thành phần đối tượng 

=== "Java"
    ```java
    public class CustomAdapter extends ArrayAdapter<Pair<String, String>> implements View.OnClickListener {
        private ArrayList<Pair<String, String>> mData;
        Context mContext;
        int mLayout = 0;

        // Construct
        public CustomAdapter(Context context, int resource, ArrayList<Pair<String,String>> data) {
            super(context, resource, data);
            this.mContext = context;
            this.mLayout = resource;
        }

        @Override
        public void onClick(View view) {
            // maybe nothing
        }


        @Override
        public View getView(int position, View convertView, ViewGroup parent) {
            if (convertView == null) {
                LayoutInflater inflater = LayoutInflater.from(mContext);
                convertView = inflater.inflate(mLayout, parent, false);
            }

            Pair<String, String> dataModel = getItem(position);
            TextView textView1 = (TextView) convertView.findViewById(R.id.text1);
            TextView textView2 = (TextView) convertView.findViewById(R.id.text2);
            if(null!=dataModel.first) {
                textView1.setText(dataModel.first);
            }
            if(null!=dataModel.second) {
                textView2.setText(dataModel.second);
            }
            // Return the completed view to render on screen
            return convertView;
        }
    }
    ```
=== "Kotlin"
    TO_DO

Sử dụng

=== "Java"
    ```java
        ArrayList<Pair<String,String>> list = new ArrayList<Pair<String,String>>();
        list.add(new Pair<String, String>("Apple", "Detail: Red when it done"));
        list.add(new Pair<String, String>("Banana", "Detail: Have yellow color when done"));
        list.add(new Pair<String, String>("Cherry", "Detail: I don't like this fruit"));
        list.add(new Pair<String, String>("Lighter", "Detail: Make a fire"));
        list.add(new Pair<String, String>("Wow wow wow ...", "Detail: The sound"));


        CustomAdapter adapter = new CustomAdapter(
            getApplicationContext(),
            R.layout.listview_custom_1,
            list
        );

        ListView listView = findViewById(R.id.listview);
        listView.setAdapter(adapter);
    ```
=== "Kotlin"
    TO_DO