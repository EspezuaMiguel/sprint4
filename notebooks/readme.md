# EDA.ipynb  

full information include image is too big to be loading on the github it is compress form

you can find some images or run all again to see the images also I add the html file or open web app

Thank you for understanding.


<img src='images/table.png'>
<img src="images/bar_chart.png">

<img src='images/Histogram_condition_comparison.png'>

<img src='images/two_branch_comparison.png'>


<html './EDA.html'>
<html>

<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">

<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h1 id="Sprint-4-Project">Sprint 4 Project<a class="anchor-link" href="#Sprint-4-Project">&#182;</a></h1><h2 id="Project-description">Project description<a class="anchor-link" href="#Project-description">&#182;</a></h2><p>Develop a web application toa cloud service be acceble by public</p>
<ul>
<li>load the code and result to github.com  (<a href="https://github.com/EspezuaMiguel/sprint4.git">https://github.com/EspezuaMiguel/sprint4.git</a>)</li>
<li>web application will display in render.com cloud  (<a href="https://test01-pbtt.onrender.com/">https://test01-pbtt.onrender.com/</a>)</li>
<li>the dataset will information come from car advertisemnt (vehicles_us.csv)</li>
<li>load the informatio, preprocessing and used plotly-express library for histogram and scattetplots.</li>
<li>generate the app.py script for deploy the chart on web app.</li>
</ul>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>the project instruction are as folow 
Exploratory Data Analysis</p>
<ol>
<li>Create an EDA.ipynb Jupyter notebook in VS Code.</li>
<li>Save the notebook in the notebooks directory of your project.</li>
<li>Perform some basic exploratory analysis of the dataset in the notebook.</li>
<li>Create a couple of histograms and scatterplots using plotly-express library.</li>
</ol>
<p>Note:
if you are using the car advertisement dataset, it won’t be sufficient to</p>
<ul>
<li>simply recreate the plots described in the blog post to complete the project. You’ll have to get creative and come up with your own plots and histograms.</li>
<li>it’s often very convenient to experiment with data visualizations in Jupyter, and then copy-paste code into a web application file later</li>
</ul>

</div>
</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>Table Example</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">plotly.graph_objects</span> <span class="k">as</span> <span class="nn">go</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">plotly.express</span> <span class="k">as</span> <span class="nn">px</span>

<span class="kn">import</span> <span class="nn">re</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;../vehicles_us.csv&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">display</span><span class="p">(</span><span class="n">df_vehicles</span><span class="p">[:</span><span class="mi">5</span><span class="p">])</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output " data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>model_year</th>
      <th>model</th>
      <th>condition</th>
      <th>cylinders</th>
      <th>fuel</th>
      <th>odometer</th>
      <th>transmission</th>
      <th>type</th>
      <th>paint_color</th>
      <th>is_4wd</th>
      <th>date_posted</th>
      <th>days_listed</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9400</td>
      <td>2011.0</td>
      <td>bmw x5</td>
      <td>good</td>
      <td>6.0</td>
      <td>gas</td>
      <td>145000.0</td>
      <td>automatic</td>
      <td>SUV</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>2018-06-23</td>
      <td>19</td>
    </tr>
    <tr>
      <th>1</th>
      <td>25500</td>
      <td>NaN</td>
      <td>ford f-150</td>
      <td>good</td>
      <td>6.0</td>
      <td>gas</td>
      <td>88705.0</td>
      <td>automatic</td>
      <td>pickup</td>
      <td>white</td>
      <td>1.0</td>
      <td>2018-10-19</td>
      <td>50</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5500</td>
      <td>2013.0</td>
      <td>hyundai sonata</td>
      <td>like new</td>
      <td>4.0</td>
      <td>gas</td>
      <td>110000.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>red</td>
      <td>NaN</td>
      <td>2019-02-07</td>
      <td>79</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1500</td>
      <td>2003.0</td>
      <td>ford f-150</td>
      <td>fair</td>
      <td>8.0</td>
      <td>gas</td>
      <td>NaN</td>
      <td>automatic</td>
      <td>pickup</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2019-03-22</td>
      <td>9</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14900</td>
      <td>2017.0</td>
      <td>chrysler 200</td>
      <td>excellent</td>
      <td>4.0</td>
      <td>gas</td>
      <td>80903.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>black</td>
      <td>NaN</td>
      <td>2019-04-02</td>
      <td>28</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 51525 entries, 0 to 51524
Data columns (total 13 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   price         51525 non-null  int64  
 1   model_year    47906 non-null  float64
 2   model         51525 non-null  object 
 3   condition     51525 non-null  object 
 4   cylinders     46265 non-null  float64
 5   fuel          51525 non-null  object 
 6   odometer      43633 non-null  float64
 7   transmission  51525 non-null  object 
 8   type          51525 non-null  object 
 9   paint_color   42258 non-null  object 
 10  is_4wd        25572 non-null  float64
 11  date_posted   51525 non-null  object 
 12  days_listed   51525 non-null  int64  
dtypes: float64(4), int64(2), object(7)
memory usage: 5.1+ MB
</pre>
</div>
</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>of total 51525 rows was read from dataset,  13 columns with information fro single vehicles posted. this record give the information of details for each vehicle, however some rows were no completed o miss inforamtion fro each columns.</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">=</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;model&#39;</span><span class="p">,</span> <span class="n">group_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span><span class="n">x</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">median</span><span class="p">()))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;cylinders&#39;</span><span class="p">]</span><span class="o">=</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;model&#39;</span><span class="p">,</span> <span class="n">group_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;cylinders&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span><span class="n">x</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">median</span><span class="p">()))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;odometer&#39;</span><span class="p">]</span><span class="o">=</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;model_year&#39;</span><span class="p">],</span> <span class="n">group_keys</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;odometer&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">x</span><span class="p">:</span><span class="n">x</span><span class="o">.</span><span class="n">fillna</span><span class="p">(</span><span class="n">x</span><span class="o">.</span><span class="n">median</span><span class="p">()))</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39; Detection  outlier by price&#39;&#39;&#39;</span>
<span class="c1"># IQR</span>
<span class="c1"># Calculate the upper and lower limits</span>
<span class="n">Q1</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">quantile</span><span class="p">(</span><span class="mf">0.25</span><span class="p">)</span>
<span class="n">Q3</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">quantile</span><span class="p">(</span><span class="mf">0.75</span><span class="p">)</span>
<span class="n">IQR</span> <span class="o">=</span> <span class="n">Q3</span> <span class="o">-</span> <span class="n">Q1</span>
<span class="n">lower</span> <span class="o">=</span> <span class="n">Q1</span> <span class="o">-</span> <span class="mf">1.5</span><span class="o">*</span><span class="n">IQR</span>
<span class="n">upper</span> <span class="o">=</span> <span class="n">Q3</span> <span class="o">+</span> <span class="mf">1.5</span><span class="o">*</span><span class="n">IQR</span>

<span class="c1"># Create arrays of Boolean values indicating the outlier rows</span>
<span class="n">upper_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">&gt;=</span><span class="n">upper</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">lower_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">&lt;=</span><span class="n">lower</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1"># Removing the outliers</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">upper_array</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">lower_array</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(</span><span class="n">drop</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="sd">&#39;&#39;&#39; Detection &#39;&#39;&#39;</span>
<span class="c1"># IQR</span>
<span class="c1"># Calculate the upper and lower limits</span>
<span class="n">Q1</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">quantile</span><span class="p">(</span><span class="mf">0.25</span><span class="p">)</span>
<span class="n">Q3</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">quantile</span><span class="p">(</span><span class="mf">0.75</span><span class="p">)</span>
<span class="n">IQR</span> <span class="o">=</span> <span class="n">Q3</span> <span class="o">-</span> <span class="n">Q1</span>
<span class="n">lower</span> <span class="o">=</span> <span class="n">Q1</span> <span class="o">-</span> <span class="mf">1.5</span><span class="o">*</span><span class="n">IQR</span>
<span class="n">upper</span> <span class="o">=</span> <span class="n">Q3</span> <span class="o">+</span> <span class="mf">1.5</span><span class="o">*</span><span class="n">IQR</span>

<span class="c1"># Create arrays of Boolean values indicating the outlier rows</span>
<span class="n">upper_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">&gt;=</span><span class="n">upper</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">lower_array</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">where</span><span class="p">(</span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model_year&#39;</span><span class="p">]</span><span class="o">&lt;=</span><span class="n">lower</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>

<span class="c1"># Removing the outliers</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">upper_array</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="n">lower_array</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(</span><span class="n">drop</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h4 id="fill-in-the-missing-values">fill in the missing values<a class="anchor-link" href="#fill-in-the-missing-values">&#182;</a></h4><ul>
<li>model_year: group by model fill by median year (don4t drop rows with NaNs in this column)</li>
<li>cylindres: group by model fill by median cylindres</li>
<li>odometer: group by model year(or year+model) fill by median(mean)</li>
<li>odometer As a recommendation - it's better to remove model year and price outliers to make your scatterplots more informative.</li>
</ul>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1">#Check drop values and fill nan</span>
<span class="n">df_vehicles</span><span class="o">.</span><span class="n">info</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>&lt;class &#39;pandas.core.frame.DataFrame&#39;&gt;
RangeIndex: 49085 entries, 0 to 49084
Data columns (total 13 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   price         49085 non-null  int64  
 1   model_year    49085 non-null  float64
 2   model         49085 non-null  object 
 3   condition     49085 non-null  object 
 4   cylinders     49085 non-null  float64
 5   fuel          49085 non-null  object 
 6   odometer      49085 non-null  float64
 7   transmission  49085 non-null  object 
 8   type          49085 non-null  object 
 9   paint_color   40251 non-null  object 
 10  is_4wd        23875 non-null  float64
 11  date_posted   49085 non-null  object 
 12  days_listed   49085 non-null  int64  
dtypes: float64(4), int64(2), object(7)
memory usage: 4.9+ MB
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="p">[</span><span class="n">go</span><span class="o">.</span><span class="n">Table</span><span class="p">(</span>
    <span class="n">header</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">values</span><span class="o">=</span><span class="nb">list</span><span class="p">(</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">columns</span><span class="p">),</span>
                <span class="n">fill_color</span><span class="o">=</span><span class="s1">&#39;paleturquoise&#39;</span><span class="p">,</span>
                <span class="n">align</span><span class="o">=</span><span class="s1">&#39;left&#39;</span><span class="p">),</span>
    <span class="n">cells</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">values</span><span class="o">=</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">transpose</span><span class="p">()</span><span class="o">.</span><span class="n">values</span><span class="o">.</span><span class="n">tolist</span><span class="p">(),</span>
               <span class="n">fill_color</span><span class="o">=</span><span class="s1">&#39;lavender&#39;</span><span class="p">,</span>
               <span class="n">align</span><span class="o">=</span><span class="s1">&#39;left&#39;</span><span class="p">))</span>
<span class="p">])</span>

<span class="n">fig</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span>  <span class="o">=</span>  <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;model&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">&#39; &#39;</span><span class="p">,</span> <span class="n">n</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">expand</span><span class="o">=</span><span class="kc">True</span><span class="p">)[</span><span class="mi">0</span><span class="p">]</span>
<span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;manufacturer_count&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<p>split the column model, to add the column manufacturer in the dataframe</p>

</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">display</span><span class="p">(</span><span class="n">df_vehicles</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output " data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>model_year</th>
      <th>model</th>
      <th>condition</th>
      <th>cylinders</th>
      <th>fuel</th>
      <th>odometer</th>
      <th>transmission</th>
      <th>type</th>
      <th>paint_color</th>
      <th>is_4wd</th>
      <th>date_posted</th>
      <th>days_listed</th>
      <th>manufacturer</th>
      <th>manufacturer_count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34506</th>
      <td>3500</td>
      <td>2007.0</td>
      <td>chevrolet silverado 2500hd</td>
      <td>good</td>
      <td>8.0</td>
      <td>gas</td>
      <td>236000.0</td>
      <td>automatic</td>
      <td>pickup</td>
      <td>white</td>
      <td>NaN</td>
      <td>2019-02-01</td>
      <td>22</td>
      <td>chevrolet</td>
      <td>chevrolet</td>
    </tr>
    <tr>
      <th>39928</th>
      <td>5495</td>
      <td>2010.0</td>
      <td>volkswagen jetta</td>
      <td>excellent</td>
      <td>5.0</td>
      <td>gas</td>
      <td>53465.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>black</td>
      <td>NaN</td>
      <td>2018-10-30</td>
      <td>71</td>
      <td>volkswagen</td>
      <td>volkswagen</td>
    </tr>
    <tr>
      <th>4140</th>
      <td>7000</td>
      <td>2010.0</td>
      <td>chevrolet silverado 2500hd</td>
      <td>good</td>
      <td>8.0</td>
      <td>gas</td>
      <td>128000.0</td>
      <td>automatic</td>
      <td>pickup</td>
      <td>green</td>
      <td>1.0</td>
      <td>2019-01-04</td>
      <td>58</td>
      <td>chevrolet</td>
      <td>chevrolet</td>
    </tr>
    <tr>
      <th>40333</th>
      <td>7950</td>
      <td>2010.0</td>
      <td>honda accord</td>
      <td>excellent</td>
      <td>4.0</td>
      <td>gas</td>
      <td>121607.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>black</td>
      <td>NaN</td>
      <td>2018-06-29</td>
      <td>36</td>
      <td>honda</td>
      <td>honda</td>
    </tr>
    <tr>
      <th>24154</th>
      <td>4950</td>
      <td>2009.0</td>
      <td>honda cr-v</td>
      <td>good</td>
      <td>4.0</td>
      <td>gas</td>
      <td>131565.0</td>
      <td>automatic</td>
      <td>SUV</td>
      <td>blue</td>
      <td>NaN</td>
      <td>2018-11-30</td>
      <td>6</td>
      <td>honda</td>
      <td>honda</td>
    </tr>
    <tr>
      <th>44037</th>
      <td>1700</td>
      <td>2003.0</td>
      <td>ford explorer</td>
      <td>good</td>
      <td>6.0</td>
      <td>gas</td>
      <td>210000.0</td>
      <td>automatic</td>
      <td>SUV</td>
      <td>silver</td>
      <td>1.0</td>
      <td>2018-12-12</td>
      <td>11</td>
      <td>ford</td>
      <td>ford</td>
    </tr>
    <tr>
      <th>25741</th>
      <td>13000</td>
      <td>2010.0</td>
      <td>toyota tacoma</td>
      <td>excellent</td>
      <td>6.0</td>
      <td>gas</td>
      <td>150000.0</td>
      <td>automatic</td>
      <td>pickup</td>
      <td>silver</td>
      <td>1.0</td>
      <td>2018-12-13</td>
      <td>8</td>
      <td>toyota</td>
      <td>toyota</td>
    </tr>
    <tr>
      <th>13450</th>
      <td>14498</td>
      <td>2014.0</td>
      <td>acura tl</td>
      <td>excellent</td>
      <td>6.0</td>
      <td>gas</td>
      <td>84152.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>black</td>
      <td>NaN</td>
      <td>2018-12-14</td>
      <td>38</td>
      <td>acura</td>
      <td>acura</td>
    </tr>
    <tr>
      <th>19441</th>
      <td>3900</td>
      <td>2004.0</td>
      <td>honda accord</td>
      <td>fair</td>
      <td>4.0</td>
      <td>gas</td>
      <td>156640.0</td>
      <td>automatic</td>
      <td>sedan</td>
      <td>silver</td>
      <td>NaN</td>
      <td>2018-12-02</td>
      <td>87</td>
      <td>honda</td>
      <td>honda</td>
    </tr>
    <tr>
      <th>38636</th>
      <td>24500</td>
      <td>2017.0</td>
      <td>gmc sierra 1500</td>
      <td>like new</td>
      <td>8.0</td>
      <td>gas</td>
      <td>18000.0</td>
      <td>automatic</td>
      <td>truck</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2018-11-30</td>
      <td>27</td>
      <td>gmc</td>
      <td>gmc</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">count_vehicles</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;type&#39;</span><span class="p">,</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">],</span> <span class="n">as_index</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;manufacturer_count&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">px</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">medals_long</span><span class="p">()</span>

<span class="n">fig</span> <span class="o">=</span> <span class="n">px</span><span class="o">.</span><span class="n">bar</span><span class="p">(</span><span class="n">count_vehicles</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;manufacturer&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s2">&quot;manufacturer_count&quot;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;type&quot;</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">&#39;Number vehicles by manufacture&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;condition_count&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[</span><span class="s1">&#39;condition&#39;</span><span class="p">]</span>
<span class="n">count_conditions</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;condition&#39;</span><span class="p">,</span><span class="s1">&#39;model_year&#39;</span><span class="p">],</span> <span class="n">as_index</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;condition_count&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">fig</span> <span class="o">=</span> <span class="n">px</span><span class="o">.</span><span class="n">histogram</span><span class="p">(</span><span class="n">count_conditions</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s2">&quot;model_year&quot;</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s2">&quot;condition_count&quot;</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s2">&quot;condition&quot;</span><span class="p">,</span> <span class="n">nbins</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">&#39;Histogram - comparison by vehicles condition&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs  ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">manufacture_comparison</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">],</span> <span class="n">as_index</span><span class="o">=</span><span class="kc">False</span><span class="p">)[</span><span class="s1">&#39;manufacturer_count&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>

<span class="n">price_manufacture</span> <span class="o">=</span> <span class="n">df_vehicles</span><span class="p">[[</span><span class="s1">&#39;price&#39;</span><span class="p">,</span> <span class="s1">&#39;manufacturer&#39;</span><span class="p">]]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">price_manufacturetwo</span> <span class="o">=</span> <span class="n">price_manufacture</span><span class="p">[(</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span>  <span class="s1">&#39;bmw&#39;</span><span class="p">)</span> <span class="o">|</span> <span class="p">(</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span>  <span class="s1">&#39;toyota&#39;</span><span class="p">)]</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>



<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output " data-mime-type="text/html">
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>price</th>
      <th>manufacturer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>9400</td>
      <td>bmw</td>
    </tr>
    <tr>
      <th>6</th>
      <td>12990</td>
      <td>toyota</td>
    </tr>
    <tr>
      <th>21</th>
      <td>5250</td>
      <td>toyota</td>
    </tr>
    <tr>
      <th>31</th>
      <td>11999</td>
      <td>toyota</td>
    </tr>
  </tbody>
</table>
</div>
</div>

</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># create figure</span>
<span class="n">x_1</span> <span class="o">=</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span>  <span class="s1">&#39;bmw&#39;</span><span class="p">][</span><span class="s1">&#39;price&#39;</span><span class="p">]</span>
<span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">()</span>

<span class="n">fig</span><span class="o">.</span><span class="n">add_trace</span><span class="p">(</span><span class="n">go</span><span class="o">.</span><span class="n">Histogram</span><span class="p">(</span><span class="n">histfunc</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                           <span class="n">x</span><span class="o">=</span><span class="n">x_1</span><span class="p">,</span>
                           <span class="n">name</span><span class="o">=</span><span class="s2">&quot;bmw&quot;</span><span class="p">,</span><span class="n">nbinsx</span> <span class="o">=</span> <span class="mi">50</span><span class="p">)</span>
             <span class="p">)</span>

<span class="c1">#Create a button list for the colors</span>
<span class="n">buttonlist1</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">p1</span> <span class="ow">in</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">():</span>
      <span class="n">x_11</span> <span class="o">=</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">p1</span><span class="p">][</span><span class="s1">&#39;price&#39;</span><span class="p">]</span>
      <span class="c1">#print(x_11)</span>
      <span class="c1">#print(p1, str(p1))</span>
      <span class="n">buttonlist1</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
        <span class="nb">dict</span><span class="p">(</span>
           <span class="c1"># args=[{&#39;name&#39;: str(p1) ,&#39;x&#39;:&#39;x_11&#39;}],</span>
            <span class="n">args</span><span class="o">=</span><span class="p">[{</span><span class="s1">&#39;x&#39;</span><span class="p">:[</span><span class="n">x_11</span><span class="p">],</span><span class="s1">&#39;name&#39;</span><span class="p">:[</span><span class="nb">str</span><span class="p">(</span><span class="n">p1</span><span class="p">)]}],</span>
            <span class="c1">#args=[&#39;name&#39;, str(p1)],</span>
            <span class="n">label</span><span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">p1</span><span class="p">),</span>
            <span class="n">method</span><span class="o">=</span><span class="s1">&#39;restyle&#39;</span>
            <span class="p">))</span>


<span class="c1">#Update the layout to include the dropdown menus, and to show titles etc</span>

<span class="n">updatemenus</span> <span class="o">=</span> <span class="nb">list</span><span class="p">([</span>
    <span class="nb">dict</span><span class="p">(</span><span class="n">buttons</span><span class="o">=</span><span class="n">buttonlist1</span><span class="p">,</span>
    <span class="p">)</span>
<span class="p">])</span>

<span class="c1"># Add dropdown</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">title_text</span><span class="o">=</span><span class="s1">&#39;Histogram by singles factory&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span>
    <span class="n">updatemenus</span><span class="o">=</span><span class="n">updatemenus</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">barmode</span><span class="o">=</span><span class="s1">&#39;overlay&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">maxlen</span><span class="o">=</span><span class="p">[]</span>
<span class="k">for</span> <span class="n">p2</span> <span class="ow">in</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">():</span>
      <span class="n">maxlen</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">price_manufacture</span><span class="p">[</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">p2</span><span class="p">][</span><span class="s1">&#39;price&#39;</span><span class="p">]))</span>

<span class="n">maxros</span> <span class="o">=</span>  <span class="nb">max</span><span class="p">(</span><span class="n">maxlen</span><span class="p">)</span>
<span class="c1">#new_index = pd.Index(range(maxros+1))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">maxlen</span><span class="p">))</span>

<span class="n">dfm</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="nb">range</span><span class="p">(</span><span class="n">maxros</span><span class="p">))</span>
<span class="k">for</span> <span class="n">p2</span> <span class="ow">in</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">():</span>
      <span class="n">colupd</span> <span class="o">=</span> <span class="n">price_manufacture</span><span class="p">[</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">p2</span><span class="p">][</span><span class="s1">&#39;price&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">reset_index</span><span class="p">(</span><span class="n">drop</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

      <span class="n">collen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">price_manufacture</span><span class="p">[</span><span class="n">price_manufacture</span><span class="p">[</span><span class="s1">&#39;manufacturer&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="n">p2</span><span class="p">][</span><span class="s1">&#39;price&#39;</span><span class="p">])</span>

      <span class="n">dfm</span><span class="p">[</span><span class="n">p2</span><span class="p">]</span> <span class="o">=</span> <span class="n">colupd</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>12069
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># create a figure with two place holder traces</span>
<span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span>
    <span class="p">[</span>
        <span class="n">go</span><span class="o">.</span><span class="n">Histogram</span><span class="p">(</span><span class="n">histfunc</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span><span class="n">x</span><span class="o">=</span><span class="n">dfm</span><span class="p">[</span><span class="n">dfm</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]],</span> <span class="n">meta</span><span class="o">=</span><span class="n">i</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">i</span><span class="p">,</span> <span class="n">nbinsx</span> <span class="o">=</span> <span class="mi">50</span><span class="p">,</span> <span class="n">opacity</span><span class="o">=</span><span class="mf">0.6</span><span class="p">,</span> <span class="n">histnorm</span><span class="o">=</span><span class="s1">&#39;probability density&#39;</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
    <span class="p">]</span>
<span class="p">)</span>

<span class="c1"># but data for y and name in when country is selected</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">title_text</span><span class="o">=</span><span class="s1">&#39;Normalized Histogram - Price comparison between two make vehicles&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span>
    <span class="n">updatemenus</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="n">b</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span>
            <span class="s2">&quot;y&quot;</span><span class="p">:</span> <span class="mf">1.4</span><span class="p">,</span>
            <span class="s2">&quot;active&quot;</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">&quot;buttons&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="p">{</span>
                    <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="n">c</span><span class="p">,</span>
                    <span class="s2">&quot;method&quot;</span><span class="p">:</span> <span class="s2">&quot;restyle&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;args&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">dfm</span><span class="p">[</span><span class="n">c</span><span class="p">]],</span> <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">c</span><span class="p">},</span> <span class="p">[</span><span class="n">b</span><span class="p">]],</span>
                <span class="p">}</span>
                <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">dfm</span><span class="o">.</span><span class="n">columns</span>
            <span class="p">],</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
    <span class="p">]</span>
<span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">barmode</span><span class="o">=</span><span class="s1">&#39;overlay&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[&nbsp;]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># create a figure with two place holder traces</span>
<span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span>
    <span class="p">[</span>
        <span class="n">go</span><span class="o">.</span><span class="n">Histogram</span><span class="p">(</span><span class="n">histfunc</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span><span class="n">x</span><span class="o">=</span><span class="n">dfm</span><span class="p">[</span><span class="n">dfm</span><span class="o">.</span><span class="n">columns</span><span class="p">[</span><span class="n">i</span><span class="p">]],</span> <span class="n">meta</span><span class="o">=</span><span class="n">i</span><span class="p">,</span> <span class="n">name</span><span class="o">=</span><span class="n">i</span><span class="p">,</span> <span class="n">nbinsx</span> <span class="o">=</span> <span class="mi">50</span><span class="p">,</span> <span class="n">opacity</span><span class="o">=</span><span class="mf">0.6</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
    <span class="p">]</span>
<span class="p">)</span>

<span class="c1"># but data for y and name in when country is selected</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">title_text</span><span class="o">=</span><span class="s1">&#39;Histogram - Price comparison between two make vehicles&#39;</span><span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span>
    <span class="n">updatemenus</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="n">b</span> <span class="o">/</span> <span class="mi">3</span><span class="p">,</span>
            <span class="s2">&quot;y&quot;</span><span class="p">:</span> <span class="mf">1.4</span><span class="p">,</span>
            <span class="s2">&quot;active&quot;</span><span class="p">:</span> <span class="kc">None</span><span class="p">,</span>
            <span class="s2">&quot;buttons&quot;</span><span class="p">:</span> <span class="p">[</span>
                <span class="p">{</span>
                    <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="n">c</span><span class="p">,</span>
                    <span class="s2">&quot;method&quot;</span><span class="p">:</span> <span class="s2">&quot;restyle&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;args&quot;</span><span class="p">:</span> <span class="p">[{</span><span class="s2">&quot;x&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">dfm</span><span class="p">[</span><span class="n">c</span><span class="p">]],</span> <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="n">c</span><span class="p">},</span> <span class="p">[</span><span class="n">b</span><span class="p">]],</span>
                <span class="p">}</span>
                <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">dfm</span><span class="o">.</span><span class="n">columns</span>
            <span class="p">],</span>
        <span class="p">}</span>
        <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
    <span class="p">]</span>
<span class="p">)</span>
<span class="n">fig</span><span class="o">.</span><span class="n">update_layout</span><span class="p">(</span><span class="n">barmode</span><span class="o">=</span><span class="s1">&#39;overlay&#39;</span><span class="p">)</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>





</div>

</div>

</div>

</div>
<div class="jp-Cell-inputWrapper"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput " data-mime-type="text/markdown">
<h2 id="Conclusion:">Conclusion:<a class="anchor-link" href="#Conclusion:">&#182;</a></h2><ul>
<li><p>on the preprocessing stage we fill the nan cells with media values calculated with semilar items by grouping.  for whe next columns 'model_year', 'cylinders', 'odometer'.</p>
</li>
<li><p>were drop the outler values for price and model year, were calculated the values outsite of interquartil ranges.</p>
</li>
<li><p>in order to get manufacture information were extract from model column.</p>
</li>
</ul>
<p>overoll, the dataset provide valious information acording volumen comparison of vehicles are avibles on the market. the condition of vehicles. 
the last chart help to undertand the distribution of price by comparing two branch.</p>

</div>
</div>
</body>







</html>
