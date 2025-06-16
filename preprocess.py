def preprocess_data(df):
    # Define variables
    current_year = 2021
    previous_year = 2016
    
    # Filter age data rows by provided groups.
    df_metrics = df[df['Statistic'].str.contains('years')]

    # Strip whitespaces from 'Statistic' column
    df_metrics['Statistic'] = df_metrics['Statistic'].str.lstrip()

    # Map old age groups to new age groups
    def map_age(age_str):
        """
        Maps a shorter age group to existing age group category in data.

        Parameters:
            age_str (int or float): The existing age group.

        Returns:
            str: The new age group category as a string.
                Returns 'Unknown' if the age does not fit any category.
        """
        if 'under' in age_str.lower() or '0 to 4' in age_str or '5 to 9' in age_str or '10 to 14' in age_str:
            return '0 to 14 years'
        elif '15 to 19' in age_str:
            return '15 to 19 years'
        elif any(x in age_str for x in ['20 to', '25 to', '30 to', '35 to', '40 to', '45 to', '50 to', '55 to', '60 to', '20 to 64']):
            return '20 to 64 years'
        elif any(x in age_str for x in ['65 to', '70 to', '75 to', '80 to', '85 to', '90 to', '95 to', '100']):
            return '65 years and over'
        else:
            return 'Unknown'

    df_metrics['New Statistic'] = df_metrics['Statistic'].apply(map_age)

    # Calculate age aggregates based on new mapping
    df_metrics = df_metrics.groupby(['Geographic name', 'New Statistic'])['Value'].sum().reset_index()

    # Calculate age distributions
    def calculate_age_distribution(df):
        """
        Calculates the percentage of each age group within each geographic region.
        
        Parameters:
        df (pd.DataFrame): Input DataFrame with columns ['Geographic name', 'New Statistic', 'Value']
        
        Returns:
        pd.DataFrame: DataFrame with an additional column 'Age Distribution' (%)
        """
        # Calculate the total population per geographic name
        total_per_geo = df.groupby('Geographic name')['Value'].transform('sum')
        
        # Calculate age distribution as percentage
        df['Age Distribution'] = (df['Value'] / total_per_geo) * 100
        
        return df

    df_metrics = calculate_age_distribution(df_metrics)

    # Pivot dataframe
    df_metrics = df_metrics.pivot_table(index='Geographic name', columns='New Statistic', values='Value', aggfunc='sum').reset_index()

    # Total population (Current Year)
    df_metrics['Total Population ' + str(current_year)] = df_metrics.iloc[:, 1:5].sum(axis=1).rename('Total Population')

    # Total population (Previous Year)
    df_pop_prev_yr = df.loc[df['Statistic'].str.contains('Population, ' + str(previous_year)), ['Geographic name', 'Value']].rename(columns={'Value': 'Total Population ' + str(previous_year)})
    df_metrics = df_metrics.merge(df_pop_prev_yr, on='Geographic name', how='left')

    # Population Growth (%)
    df_metrics['Population Growth (%)'] = ((df_metrics['Total Population ' + str(current_year)] - df_metrics['Total Population ' + str(previous_year)]) / df_metrics['Total Population ' + str(previous_year)]) * 100

    # Median household income
    df_med_inc = df.loc[df['Statistic'] == 'Median total income of household in {} ($)'.format(str(current_year - 1)), ['Geographic name', 'Value']].rename(columns={'Value': 'Median total income of household in ' + str(current_year - 1)})
    df_metrics = df_metrics.merge(df_med_inc, on='Geographic name', how='left')

    # Unemployment Rate
    df_unemp_rate = df.loc[df['Statistic'] == 'Unemployment rate', ['Geographic name', 'Value']].rename(columns={'Value': 'Unemployment Rate (%)'})
    df_metrics = df_metrics.merge(df_unemp_rate, on='Geographic name', how='left')

    # Sort values by population size
    df_metrics.sort_values(by='Total Population ' + str(current_year), ascending=False, inplace=True)
    df_metrics.reset_index(drop=True, inplace=True)

    return df_metrics